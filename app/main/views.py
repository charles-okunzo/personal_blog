from . import main
from flask import render_template, url_for, request, redirect
from ..requests import get_random_quotes



@main.route('/')
def index():
  rand_quote = get_random_quotes()
  title = "Welcome to my personal blogs | Be Inspired"
  return render_template('index.html', quote=rand_quote, title=title)