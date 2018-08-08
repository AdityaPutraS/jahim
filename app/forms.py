from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo,InputRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    displayname = StringField('Display name',validators=[DataRequired()])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirmPass', message = 'Password tidak sama')])
    confirmPass = PasswordField('Confirm password', validators=[InputRequired()])
    submit = SubmitField('Register')
