from . import db
from werkzeug.security import generate_password_hash, check_password_hash


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


  @property
  def password(self):
    raise AttributeError('You cannot access this password')


  @password.setter
  def password(self, password):
    self.pass_code = generate_password_hash(password)


  def verify_password(self, password):
    return check_password_hash(self.pass_code, password)


  def __repr__(self):
      return f'User {self.username}'



  