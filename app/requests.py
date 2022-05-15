import urllib.request, json
from .models import RandQuotes



quotes_url = None


def configure(app):
  global quotes_url

  quotes_url = app.config['RANDOM_QUOTE_URL']



def get_random_quotes():

  with urllib.request.urlopen(quotes_url) as url:
    quote_data = url.read()
    quote_response = json.loads(quote_data)

    if quote_response:
      quote = quote_response.get('quote')
      author = quote_response.get('author')

      new_quote = RandQuotes(author, quote)


  return new_quote