from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Passage(db.Model):
	__tablename__ = "Passage"
	__searchable__ = ['title', 'author']

	id = db.Column(db.Integer, primary_key= True)

	content= db.Column(db.String(1500), nullable=False)
	title = db.Column(db.String(128), nullable=True)
	author = db.Column(db.String(100), nullable=True)

	def to_JSON(self):
		return {
			"content": self.content,
			"title": self.title,
			"author": self.author
		}

class Title(db.Model):
	__tablename__ = "Title"

	id = db.Column (db.Integer, primary_key=True)

	title = db.Column(db.String, unique=True, nullable=False)
	
	
