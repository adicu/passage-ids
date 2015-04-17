from wtforms import TextField, TextAreaField, SubmitField, SelectField, validators, ValidationError
from flask.ext.wtf import Form

class SubmissionForm(Form):
	title = TextField("Title", [validators.Required("Please enter the title of the work.")])
	author = TextField("Author", [validators.Required("Please enter the author of the work.")])
	# submitter = TextField("Your Name", [validators.Required("Please enter your name.")])
	quote = TextAreaField("Quote", [validators.Required("Please enter the quote.")])
	class_type = SelectField("Class", choices = [(0, "Choose Class"), (1, "Lit Hum"), (2,"CC")], coerce = int, validators = [validators.Required("Please pick CC or Lit Hum.")])
	submit = SubmitField("Submit Passage")
