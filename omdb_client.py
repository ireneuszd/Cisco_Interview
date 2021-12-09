import json
import requests


class OmdbApiClient:
    def __init__(self, api_key):
        self.key = api_key
        self.url = 'http://www.omdbapi.com/'

    def get_movie_info(self, title):
        get_url = f'{self.url}?apikey={self.key}&t={title}'
        raw_output = requests.get(get_url)
        pretty_output = json.loads(raw_output.text)

        assert pretty_output['Response'] == 'True', \
            f'Movie: {title} was not found!'
        return pretty_output

    def get_rotten_tomato_rating(self, title):
        movie_info = self.get_movie_info(title)

        assert movie_info.get('Ratings'), f"Movie: {title} has no Ratings"
        ratings = movie_info['Ratings']

        assert 'Rotten Tomatoes' in [source['Source'] for source in ratings],\
            f"Movie: {title} has no Rotten Tomatoes ratings"

        for rating in ratings:
            if rating['Source'] == 'Rotten Tomatoes':
                return rating['Value']
