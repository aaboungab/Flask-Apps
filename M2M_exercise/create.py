from app import db, Orders, Customers, Products 

db.create_all()

anas = Customers(full_name='Anas Aboungab', email='aaboungab@gcp.com')
PS5 = Products(name='Playstation 5', price=499.99)

db.session.add(anas)
db.session.add(PS5)
db.session.commit()

order_PS5 = Orders(proudct_id=PS5.id, customer_id=anas.id)

db.session.add(order_PS5)
db.session.commit()
