from wtforms import Form, TextField, TextAreaField, SubmitField
#form to handle user quote submission
class QuoteForm(Form):
title = TextField("Title")
author = TextField("Author")
submitter = TextField("Your Name Here")
content = TextAreaField("Content")
submit = SubmitField("Submit Passage")