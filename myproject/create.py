from app import db, Users, Country

db.drop_all()
db.create_all()

testuser = Users(first_name='Grooty',last_name='Toot') # Extra: this section populates the table with an example entry
testcountry = Country(country_name='United Kingdom', country_continent='Europe')
db.session.add(testuser)
db.session.add(testcountry)
db.session.commit()
