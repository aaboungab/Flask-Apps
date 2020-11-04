from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from application.models import ToDoList

class TodoCheck:
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        all_ToDos = ToDoList.query.all()
        for todo in all_ToDos:
            if todo.name == field.data:
                raise ValidationError(self.message)

class TodoForm(FlaskForm):
    task = StringField('Task',
                validators=[
                    DataRequired(),
                    TodoCheck(message='This Todo already exsists')
                ]
           )
    submit = SubmitField('Add Todo') 
