from . import main
from flask import render_template, url_for, request, redirect



@main.route('/')
def index():


  return render_template('index.html')