
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Config:
  RANDOM_QUOTE_URL='http://quotes.stormconsultancy.co.uk/random.json'
  SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL')
  SQLALCHEMY_TRACK_MODIFICATIONS=False
  SECRET_KEY=os.getenv('SECRET_KEY')


class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL')




class DevConfig(Config):
  DEBUG=True




config_options = {
  'production': ProdConfig,
  'development': DevConfig
}