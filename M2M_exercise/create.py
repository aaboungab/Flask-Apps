from app import db, Orders, Customers, Products 

db.Create_all()

ben = Customers(first_name='Ben')
phone = Products()

db.session.add(ben)
db.session.add(phone)
db.session.commit()

order_phone = Orders(proudct_id=phone.id, customer_id=customers.id)
