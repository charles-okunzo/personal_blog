from crypt import methods
from unicodedata import category
from flask_login import login_required
from app import db
from app.main.forms import BlogForm
from app.models import BlogPost
from . import main
from flask import render_template, url_for, request, redirect
from ..requests import get_random_quotes



@main.route('/')
def index():
  rand_quote = get_random_quotes()
  title = "Welcome to my personal blogs | Be Inspired"
  return render_template('index.html', quote=rand_quote, title=title)



@main.route('/new-post', methods=['POST', 'GET'])
@login_required
def new_post():
  title = 'PersonalBlog | Create a new Blog post.'
  form = BlogForm()
  if form.validate_on_submit():
    title=form.title.data
    category=form.category.data
    post=form.post.data

    new_post_obj=BlogPost(title=title, category=category, post=post)
    db.session.add(new_post_obj)
    db.session.commit()
    
    return redirect(url_for('main.blogs_page'))

  return render_template('new_post_form.html', title=title, post_form=form)


@main.route('/posts')
def blogs_page():
  title='PersonalBlog | Blog posts'

  return render_template('blogs.html')
