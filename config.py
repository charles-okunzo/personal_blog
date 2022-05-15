
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Config:
  RANDOM_QUOTE_URL='http://quotes.stormconsultancy.co.uk/random.json'
  SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL')
  

class ProdConfig(Config):
  pass




class DevConfig(Config):
  DEBUG=True




config_options = {
  'production': ProdConfig,
  'development': DevConfig
}