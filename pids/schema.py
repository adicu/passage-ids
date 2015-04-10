from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Passage(db.Model):
	__tablename__ = "Passage"
	__searchable__ = ['title', 'author']

	id = db.Column(db.Integer, primary_key= True)

	quote= db.Column(db.String(1500), nullable=False)
	title = db.Column(db.String(128), nullable=False)
	author = db.Column(db.String(100), nullable=False)
	submitter = db.Column(db.String(200), nullable=False)
	class_type = db.Column(db.Integer(), nullable=False)

	def to_JSON(self):
		return {
			"quote": self.quote,
			"title": self.title,
			"author": self.author,
			"submitter": self.submitter
		}
