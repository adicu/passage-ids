from wtforms import TextField, TextAreaField, SubmitField, SelectField, validators, ValidationError
from flask.ext.wtf import Form

class SubmissionForm(Form):
	class_type = SelectField("Class", choices = [(0, "Choose Class"), (1, "Lit Hum"), (2,"CC")], coerce = int, validators = [validators.Required("Please pick CC or Lit Hum.")])
	title = SelectField("Title", choices= [], coerce = unicode, validators = [validators.Required("Please enter the title of the work.")])
	quote = TextAreaField("Quote", [validators.Required("Please enter the quote.")])
	submit = SubmitField("Submit Passage")
