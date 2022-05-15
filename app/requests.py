import urllib.request, json
from .models import RandQuotes



quotes_url = None


def configure(app):
  global quotes_url

  app.config['RANDOM_QUOTE_URL']