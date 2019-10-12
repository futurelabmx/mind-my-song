from wtforms import Form
from wtforms import TextField
from wtforms.validators import DataRequired


class UserForm(Form):
    email = TextField('email', validators=[DataRequired()])
    password = TextField('password', validators=[DataRequired()])
