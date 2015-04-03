__author__ = 'ADI Labs'
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import requests
from schema import Passage, Title
from passageGenerator import generatePassages
import random
from ContactForm import QuoteForm

app = Flask(__name__)
app.config["DEBUG"] = True

content = generatePassages()

@app.route("/")
def home():
	randQuote = content[random.randint(0, len(content) - 1)]
	return render_template("content.html", content2 = randQuote)

@app.route("/form", methods = ['GET', 'POST'])
def form():
	form = QuoteForm()
	if request.method == 'POST':
		quote = Passage(content = form.content, title = form.title, author = form.author)
		return render_template('form.html', form = form)
	elif request.method == 'GET':
		return render_template('form.html', form = form)

# @app.route("/login", methods = ['GET', 'POST'])
# def login():
# 	if request.method == "POST":	
# 		return render_template("login.html")

@app.route("/", methods = ['GET', 'POST'])
def bringCC():
	if request.method == "POST":
		randQuote = content[random.randint(0, len(content) - 1)]	
		return render_template("content.html", content2 = randQuote)

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found.", 404

@app.route("/login", methods = ['GET', 'POST'])
def login():
    """
    Returns an auth code after user logs in through Google+.
    :param string code: code that is passed in through Google+.
        Do not provide this yourself.
    :return: An html page with an auth code.
    :rtype: flask.Response
    """
    # Get code from params.
    code = request.args.get('code')
    if not code:
        return render_template('auth.html',
                               success=False)

    try:
        # Exchange code for email address.
        # Get Google+ ID.
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
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
        code = db.get_oauth_code_for_uni(g.cursor, uni)
        return render_template('auth.html', success=True, uni=uni, code=code)
    except Exception as e:
        # TODO: log errors3
        print e
        return render_template('auth.html',
                               success=False,
                               reason="An error occurred. Please try again.")

if __name__ == '__main__':
	app.run(host = '0.0.0.0')
