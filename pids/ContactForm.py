from wtforms import TextField, TextAreaField, SubmitField
from flask.ext.wtf import Form

class QuoteForm(Form):
	title = TextField("Title")
	author = TextField("Author")
	submitter = TextField("Your Name Here")
	content = TextAreaField("Content")
	submit = SubmitField("Submit Passage")
