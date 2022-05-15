from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, PasswordField
from wtforms.validators import Email, EqualTo, DataRequired


class SignupForm(FlaskForm):
  username = StringField('Enter username:', validators=[DataRequired()])
  email = StringField('Enter email', validators=[DataRequired(), Email()])
  password = PasswordField('Enter password', validators=[DataRequired(), EqualTo('confirm_password', 'Passwords do not match!')])
  submit = SubmitField('Signup')