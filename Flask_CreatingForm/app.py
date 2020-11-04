from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, DecimalField, SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    date = DateField('DOB (D-M-Y)',format='%d-%m-%Y')
    Integer = IntegerField('Favouriate number')
    Float = DecimalField('choose a decimal from 0-1')
    Select = SelectField('Gender', choices=[(' '), ('Male'), ('Female')])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        date = form.date.data
        Integer = form.Integer.data
        Float = form.Float.data
        Select = form.Select.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            return 'Thank you ' + first_name +' '+ last_name +' '+ ' Favouraite number: ' + str(Integer) + ' & ' + str(Float)

    return render_template('home.html', form=form, message=error)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')
