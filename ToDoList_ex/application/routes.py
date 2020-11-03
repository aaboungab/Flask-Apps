from application import app,db
from application.models import ToDoList

@app.route('/')
def home():
	all_ToDo = ToDoList.query.all()
	all_ToDo_list=""
	for ToDo in all_ToDo:
		all_ToDo_list+="<br>" + ToDo.name
	return all_ToDo_list


@app.route('/add/<newToDo>')
def add(newToDo):
	new_ToDo = ToDoList(name=newToDo)
	db.session.add(new_ToDo)
	db.session.commit()
	return "Added new ToDo added into list"

@app.route('/complete')
def complete():

@app.route('/incomplete')
def incomplete():

@app.route('update')
def update():
	first_ToDo = ToDoList.query.first()
	
	db.session.commit()
	return  

@app.route('/delete')
def delete():
