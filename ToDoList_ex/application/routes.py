from flask import render_template, redirect, url_for

from application import app,db
from application.models import ToDoList

@app.route('/')
def index():
    all_ToDo = ToDoList.query.all()
    return render_template('index.html', all_ToDo=all_ToDo)


@app.route('/add')
def add():
    new_ToDo = ToDoList(name='New ToDo')
    db.session.add(new_ToDo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:ToDo_id>')
def complete(ToDo_id):
    ToDo_to_update = ToDoList.query.get(ToDo_id)
    ToDo_to_update.complete = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<int:ToDo_id>')
def incomplete(ToDo_id):
    ToDo_to_update = ToDoList.query.get(ToDo_id)
    ToDo_to_update.complete = False
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/update/<task>')
def update(task):
    ToDo_to_update = ToDoList.query.first()
    ToDo_to_update.task = task
    db.session.commit()
    return redirect(url_for('index')) 

@app.route('/delete/<int:ToDo_id>')
def delete(ToDo_id):
    ToDo_to_delete = ToDoList.query.get(ToDo_id)
    db.session.delete(ToDo_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

