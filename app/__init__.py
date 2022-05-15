from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()



def create_app(config_name):


  app = Flask(__name__)


  #app configurations
  app.config.from_object(config_options[config_name])

  from .requests import configure
  configure(app)


  #initialise extension
  bootstrap.init_app(app)
  db.init_app(app)
  login_manager.init_app(app)


  #register blueprint
  from app.main import main as main_blueprint
  app.register_blueprint(main_blueprint)



  return app