from flask import render_template, redirect, url_for

from application import app,db
from application.models import ToDoList
from application.forms import TodoForm

@app.route('/')
def index():
    all_ToDo = ToDoList.query.all()
    return render_template('index.html', all_ToDo=all_ToDo)


@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = TodoForm()
    if form.validate_on_submit():
        new_todo = ToDoList(name=form.task.data)  
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

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


@app.route('/update/<int:ToDo_id>', methods=['GET', 'POST'])
def update(ToDo_id):
    form = TodoForm()
    ToDo_to_update = ToDoList.query.get(ToDo_id)
    if form.validate_on_submit():
        ToDo_to_update.name = form.task.data
        db.session.commit()
        return redirect(url_for('index')) 
    return render_template('update.html', form=form)

@app.route('/delete/<int:ToDo_id>')
def delete(ToDo_id):
    ToDo_to_delete = ToDoList.query.get(ToDo_id)
    db.session.delete(ToDo_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

