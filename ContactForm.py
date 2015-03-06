from flaskext.wtf import Form, TextField, TextAreaField, SubmitField



#form to handle user quote submission
class QuoteForm(Form):
	title = TextField("Title")
	author = TextField("Author")
	submitter = TextField("Your Name Here")
	passage = TextAreaField("Passage")
	submit = SubmitField("Submit Passage")
