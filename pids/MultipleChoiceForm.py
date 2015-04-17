from wtforms import RadioField, SubmitField, validators, ValidationError
from flask.ext.wtf import Form

class MultipleChoiceForm(Form):
	choices = RadioField("What work is the quote from?", coerce = int, validators = [validators.Required("Please select a work.")])
	submit = SubmitField("Submit Answer")
