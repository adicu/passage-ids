from flaskext.wtf import Form, TextField, TextAreaField, SubmitField

__init__()

#form to handle user quote submission
class QuoteForm(Form):
	title = StringField("Title", [Required(message= "Provide the title of the work.")])
	author = StringField("Author"
	submitter = StringField("Your Name Here", [Required(message= "Input your name. This will be kept private.")]
	passage = TextAreaField("Passage", [Required(message = "Input the text of the passage.")])
    submit = SubmitField("Submit Passage")

