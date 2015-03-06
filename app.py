__author__ = 'ADI Labs'
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import requests
from schema import Passage, Title
from passageGenerator import generatePassages

app = Flask(__name__)
app.config["DEBUG"] = True

# print(passages[0].content)

@app.route("/")
def home():
	content = generatePassages()
	return render_template("content.html", content2 = content)

@app.route("/login", methods = ['GET', 'POST'])
def login():
	if request.method == "POST":	
		return render_template("login.html")


@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found.", 404

if __name__ == '__main__':
	app.run(host = '0.0.0.0')
