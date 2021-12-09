from decouple import config
import sys

from omdb_client import OmdbApiClient


if __name__ == '__main__':
    if len(sys.argv) == 1:
        raise ValueError("Unsupported amount of arguments provided")
    omdb_client = OmdbApiClient(config('OMDB_KEY'))

    rating = omdb_client.get_rotten_tomato_rating(sys.argv[1])
    print(f'Rotten Tomato rating for movie: {sys.argv[1]} is:\n {rating}')
