from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Email, EqualTo, DataRequired, ValidationError
from ..models import User

class SignupForm(FlaskForm):
  username = StringField('Enter username:', validators=[DataRequired()])
  email = StringField('Enter email', validators=[DataRequired(), Email()])
  password = PasswordField('Enter password', validators=[DataRequired(), EqualTo('confirm_password', 'Passwords do not match!')])
  submit = SubmitField('Sign Up')


  def validate_username(self, data_field):
    if User.query.filter_by(username = data_field.data).first():
      raise ValidationError('Username already exists')


  def validate_email(self, data_field):
    if User.query.filter_by(email=data_field.data).first():
      raise ValidationError('This email has already been used')



class LoginForm(FlaskForm):
  email = StringField('Enter your email:', validators=[DataRequired(), Email()])
  password = PasswordField('Enter your password:', validators=[DataRequired()])
  remember = BooleanField('Remember me')
  submit  = SubmitField('Sign In')