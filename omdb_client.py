import requests


class OmdbApiClient:
  def __init__(self, api_key):
    self.key = api_key
    self.url = 'http://www.omdbapi.com/'
        
  def get_movie_info(self, title):
    get_url = f'{self.url}?apikey={self.key}&t={title}' 
    raw_output = requests.get(get_url)
    return raw_output.text
    
  def get rotten_tomato_rating(title):
    pass
