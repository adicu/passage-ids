from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError
from flask.ext.wtf import Form

class QuoteForm(Form):
	title = TextField("Title", [validators.Required("Please enter the title of the work.")])
	author = TextField("Author", [validators.Required("Please enter the author of the work.")])
	submitter = TextField("Your Name Here", [validators.Required("Please enter your name.")])
	content = TextAreaField("Content", [validators.Required("Please enter the quote.")])
	submit = SubmitField("Submit Passage")
