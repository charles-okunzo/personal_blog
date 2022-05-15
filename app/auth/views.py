from app import db
from flask import render_template, redirect,url_for,request
from app.models import User
from . import auth
from .forms import SignupForm, LoginForm






@auth.route('/signup', methods=['GET', 'POST'])
def signup():
  title = 'PersonalBlog | Sign Up'
  form = SignupForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()
    

    return redirect(url_for('auth.login'))

  return render_template('signup.html', login_form=form, title=title)