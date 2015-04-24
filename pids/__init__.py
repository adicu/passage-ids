__author__ = 'ADI Labs'
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash, json, session, redirect, g
from flask.ext.session import Session
import requests
from schema import db, Passage, User
import random
from flask.ext.sqlalchemy import SQLAlchemy
from oauth2client.client import flow_from_clientsecrets
import httplib2
import re
from SubmissionForm import SubmissionForm
from MultipleChoiceForm import MultipleChoiceForm
from categories import lithum, lithum_titles

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


@app.before_request
def lookup_current_uni():
    g.uni = None
    if 'gplus_id' in session:
        gplus_id = session['gplus_id']
        user=User.query.filter_by(gplus_id=gplus_id).all()
        # if user is not None:    
        #     g.uni = user[0].uni
        #     print g.uni
@app.before_request
def before_request():
    if session.get('type', None) is None:
        session['type'] = 0
    if session.get('form', None) is None:
        session['form'] = 0

@app.route("/")
def home():
    form = MultipleChoiceForm()
    if session['type'] is 0:
        content = Passage.query.all()
        randQuote = content[random.randint(0, len(content) - 1)]
    else:
        content = Passage.query.filter_by(class_type=session['type']).all()
        randQuote = content[random.randint(0, len(content) - 1)]
    category = randQuote.category
    choices = []
    for i in range(len(lithum["fall"]["Greek Tragedy"])):
        choices.append((i, lithum["fall"]["Greek Tragedy"][i]))
    form.choices.choices = choices
    return render_template('content.html', content2=randQuote, form=form)

@app.route("/CC", methods = ['POST'])
def setCC():
    if request.method == "POST":
        session['type'] = 2
        return redirect('/')

@app.route("/LitHum", methods = ['POST'])
def setLH():
    if request.method == "POST":
        session['type'] = 1
        return redirect('/')

@app.route("/form", methods = ['GET', 'POST'])
def form():
    form = SubmissionForm()
    form.title.choices = [("Choose", "Choose Title")] + lithum_titles["fall"] + lithum_titles["spring"]
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('form.html', form=form)
        if form.class_type.data == 0 or  form.title.data == "Choose":
            if form.class_type.data == 0:
                flash("Please pick CC or Lit Hum.")
            if form.title.data is "Choose":
                flash("Please enter the title of the work.")
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
        return render_template('form.html', form = form)
    elif request.method == 'GET':
        return render_template('form.html', form = form)

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page does not exist", 404

@app.route("/login", methods = ['GET', 'POST'])
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
    db.session.add(User(uni = uni, gplus_id = gplus_id))
    db.session.commit()

    session['gplus_id'] = gplus_id

    # print passageInfo
    return render_template('auth.html', success=True, uni=uni, code=code)
    # return render_template('content.html', loggedIn = True, uni = uni)

def run():
    """Runs the app."""
    app.run(host=app.config.get('HOST'), port=app.config.get('PORT'))
