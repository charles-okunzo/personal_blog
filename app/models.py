from . import db


class RandQuotes:


  def __init__(self,author, quote):
      self.author = author
      self.quote = quote




class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(128), nullable=False, unique=True)
  pass_code = db.Column(db.String(128), nullable=False, unique=True)


  def __repr__(self):
      return f'User {self.username}'


  