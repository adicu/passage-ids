from wtforms import TextField, TextAreaField, SubmitField
from flask.ext.wtf import Form

#form to handle user quote submission
class QuoteForm(Form):
	title = TextField("Title")
	author = TextField("Author")
	submitter = TextField("Your Name Here")
	content = TextAreaField("Content")
	submit = SubmitField("Submit Passage")