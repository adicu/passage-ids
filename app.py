__author__ = 'ADI Labs'
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import requests
from schema import Passage, Title
# from ContactForm import QuoteForm

app = Flask(__name__)
app.config["DEBUG"] = True

quote = Passage(content="Lorem ipsum", title="Iliad", author="Ken")
print(quote.content)

@app.route("/")
def home():
	# if request.form['button'] == 'login':
	# 	print("login clicked")
	# 	login()
	return render_template("content.html")

@app.route("/login", methods = ['GET', 'POST'])
def login():
	if request.method == "POST":	
		return render_template("login.html")
# def display_passage():
# 	if request.method == 'POST':
#         if request.form['submit'] == 'Do Something':
#             pass # do something
#         elif request.form['submit'] == 'Do Something Else':
#             pass # do something else
#         else:
#             pass # unknown
#     # elif request.method == 'GET':

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found.", 404

if __name__ == '__main__':
	app.run(host = "0.0.0.0")
