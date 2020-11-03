from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:11@34.89.108.42/M2M_exercise'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

class Customers(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)

class Orders(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
	customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)

class Products(db.Model):
	id = db.Column(db.integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	price = db.Column(db.Float, nullable=False)
	orders = db.relationship('Orders', backref='product')
	
