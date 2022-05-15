from flask_wtf import FlaskForm
from sqlalchemy import Text
from wtforms import StringField,SelectField,TextAreaField, SubmitField
from wtforms.validators import DataRequired



class BlogForm(FlaskForm):
  title = StringField('Title:', validators=[DataRequired()])
  category = SelectField('Category:', choices=[('Lifestyle'), ('Design'), ('Career')])
  post = TextAreaField('Your post:', validators=[DataRequired()])
  submit = SubmitField('Post')