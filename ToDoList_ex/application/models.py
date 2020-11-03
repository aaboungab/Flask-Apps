from application import db

class ToDoList(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	complete= db.Column(db.Boolean, default=False)
