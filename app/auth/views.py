
from flask_login import login_required, login_user, logout_user
from app import db
from flask import render_template, redirect,url_for,request,flash
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
    

    return redirect(url_for('auth.signin'))

  return render_template('auth/signup.html', login_form=form, title=title)


@auth.route('/login', methods=['POST','GET'])
def signin():
  title = 'PersonalBlog | Sign In'
  form= LoginForm()
  if form.validate_on_submit():
    user=User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user, form.remember.data)
      return redirect(request.args.get('next') or url_for('main.index'))
    flash('Invalid username or password')

  return render_template('auth/signin.html', signin_form=form, title=title)


@auth.route('/logout')
@login_required
def signout():
  logout_user()

  return redirect(url_for('main.index'))