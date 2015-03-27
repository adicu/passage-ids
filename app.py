__author__ = 'ADI Labs'
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import requests
from schema import Passage, Title
import random
from flask.ext.sqlalchemy import SQLAlchemy
from ContactForm import QuoteForm


app = Flask(__name__)
db = SQLAlchemy(app)

app.config["DEBUG"] = True

@app.route("/")
def home():
	content = Passage.query.all()
	randQuote = content[random.randint(0, len(content) - 1)]
	return render_template("content.html", content2 = randQuote)


@app.route("/form", methods = ['GET', 'POST'])
def form():
	form = QuoteForm()
	if request.method == 'POST':
		quote = Passage(content = form.content, title = form.title, author = form.author)
		db.session.add(quote)
		db.session.commit()
		return render_template('form.html', form = form)
	elif request.method == 'GET':
		return render_template('form.html', form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
	if request.method == "POST":	
		return render_template("login.html")

@app.route("/", methods = ['GET', 'POST'])
def bringCC():
	if request.method == "POST":
		randQuote = content[random.randint(0, len(content) - 1)]	
		return render_template("content.html", content2 = randQuote)

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found.", 404

if __name__ == '__main__':
	app.run(host = '0.0.0.0')
