__author__ = 'ADI Labs'
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.config["DEBUG"] = True




@app.route("/")
def home():
	return render_template("index.html")

# def display_passage():
# 	if request.method == 'POST':
#         if request.form['submit'] == 'Do Something':
#             pass # do something
#         elif request.form['submit'] == 'Do Something Else':
#             pass # do something else
#         else:
#             pass # unknown
#     # elif request.method == 'GET':

if __name__ == '__main__':
	app.run(host = "0.0.0.0")
