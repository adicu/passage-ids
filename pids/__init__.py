import httplib2
import re
import requests
import random
from flask import Flask, render_template, request, flash, json, session, redirect, g
from flask.ext.session import Session
from schema import db, Passage, User
from flask.ext.sqlalchemy import SQLAlchemy
from oauth2client.client import flow_from_clientsecrets
from SubmissionForm import SubmissionForm
from MultipleChoiceForm import MultipleChoiceForm
from categories import lithum_categories, lithum_titles, lithum_authors_categories
import datetime

__author__ = 'ADI Labs'
# -*- coding: utf-8 -*-

def create_app():
    app = Flask(__name__)
    app.config.from_object('pids.config')
    db.init_app(app)
    print app.config['HOST']
    return app, db

app, db = create_app()

app.secret_key = 'development key'

passage_info = None
sess = Session()

def multiple_choice(randQuote):
    current_sem = session['semester']
    category = randQuote.category
    choices = [None, None, None, None, None]
    answer = randQuote.title
    choices[random.randint(0, len(choices) - 1)] = (answer, answer)
    same_category = lithum_categories[current_sem][randQuote.category]
    counter = 0
    #ugly code that populates empty choices with others in same category
    while None in choices:
        counter +=1
        if counter is len(same_category):
            break
        potential_choice = same_category[random.randint(0, len(same_category) - 1)]
        while (potential_choice, potential_choice) in choices:
            potential_choice = same_category[random.randint(0, len(same_category) - 1)]
        choices[choices.index(None)] = (potential_choice, potential_choice)
    other_titles = lithum_titles[current_sem]
    #ugly code that populates empty choices with random titles from same sem
    while None in choices:
        potential_choice = other_titles[random.randint(0, len(other_titles) - 1)]
        while potential_choice in choices:
            potential_choice = other_titles[random.randint(0, len(other_titles) - 1)]
        choices[choices.index(None)] = potential_choice
        potential_choice = other_titles[random.randint(0, len(other_titles) - 1)]
    return {
        "choices": choices,
        "answer": answer
    }

@app.before_request
def lookup_current_uni():
    g.uni = None
    g.loggedIn = False
    if 'gplus_id' in session:
        gplus_id = session['gplus_id']
        user = User.query.filter_by(gplus_id=gplus_id).all()
        if user is not None:
            g.uni = user[0].uni
            g.loggedIn = True


@app.before_request
def before_request():
    if session.get('type', None) is None:
        session['type'] = 0
    if session.get('form', None) is None:
        session['form'] = 0
    if session.get('semester', None) is None:
        month = datetime.datetime.now().month
        if moznth < 6:
            session['semester'] = 'spring'
        else:
            session['semester'] = 'fall'


@app.route("/")
def home():
    current_sem = session['semester']
    form = MultipleChoiceForm()
    if session['type'] is 0:
        content = Passage.query.filter_by(semester=current_sem).all()
        randQuote = content[random.randint(0, len(content) - 1)]
    else:
        content = Passage.query.filter_by(class_type=session['type']).filter_by(semester=current_sem).all()
        randQuote = content[random.randint(0, len(content) - 1)]
    json = multiple_choice(randQuote)
    form.choices.choices = json['choices']
    return render_template('content.html', content2=randQuote, form=form)




@app.route("/answer", methods = ['POST'])
def submit():
    return render_template('content.html')

@app.route("/CC", methods = ['POST'])
def setCC():
    if request.method == "POST":
        session['type'] = 2
        return redirect('/')


@app.route("/LitHum", methods=['POST'])
def setLH():
    if request.method == "POST":
        session['type'] = 1
        return redirect('/')


@app.route("/form", methods=['GET', 'POST'])
def form():
    form = SubmissionForm()
    form.title.choices = [("Choose", "Choose Title")] + lithum_titles["fall"] + lithum_titles["spring"]
    if request.method == 'POST':
        if form.class_type.data == 0:
            form.class_type.data = None
        if form.title.data == "Choose":
            form.title.data = None
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('form.html', form=form)

        quote = Passage(quote=form.quote.data,
                        title=form.title.data,
                        submitter=form.submitter.data,
                        class_type=form.class_type.data)
        db.session.add(quote)
        db.session.commit()
        form.quote.data = None
        form.title.data = "Choose"
        form.class_type.data = 0
        return render_template('form.html', form=form)
    elif request.method == 'GET':
        return render_template('form.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    Returns an auth code after user logs in through Google+.
    :param string code: code that is passed in through Google+.
        Do not provide this yourself.
    :return: An html page with an auth code.
    :rtype: flask.Response
    """
    CU_EMAIL_REGEX = r"^(?P<uni>[a-z\d]+)@.*(columbia|barnard)\.edu$"
    # Get code from params.
    code = request.args.get('code')
    if not code:
        return render_template('auth.html', success=False)
    # Exchange code for email address.
    # Get Google+ ID.
    oauth_flow = flow_from_clientsecrets('pids/secrets.json', scope='')

    oauth_flow.redirect_uri = 'postmessage'
    credentials = oauth_flow.step2_exchange(code)
    gplus_id = credentials.id_token['sub']

    # Get first email address from Google+ ID.
    http = httplib2.Http()
    http = credentials.authorize(http)

    h, content = http.request('https://www.googleapis.com/plus/v1/people/' + gplus_id, 'GET')
    data = json.loads(content)
    email = data["emails"][0]["value"]
    # Verify email is valid.
    regex = re.match(CU_EMAIL_REGEX, email)

    if not regex:
        return render_template('auth.html',
                               success=False,
                               reason="You need to log in with your "
                               + "Columbia or Barnard email! You logged "
                               + "in with: "
                               + email)

    # Get UNI and ask database for code.
    uni = regex.group('uni')
    db.session.add(User(uni=uni, gplus_id=gplus_id))
    db.session.commit()

    session['gplus_id'] = gplus_id

    return render_template('auth.html', success=True, uni=uni, code=code)


@app.route("/logout", methods=['POST'])
def logout():
    g.loggedIn = False
    g.uni = None
    del session['gplus_id']
    return home()


@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page does not exist", 404


def run():
    """Runs the app."""
    app.run(host=app.config.get('HOST'), port=app.config.get('PORT'))
