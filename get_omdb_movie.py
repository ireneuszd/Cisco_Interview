import sys

from omdb_client import OmdbApiClient


if __name__ == '__main__':
    if len(sys.argv) == 1:
        raise ValueError("Unsupported amount of arguments provided")
    omdb_key = '875f3794'
    omdb_client = OmdbApiClient(omdb_key)
    print(omdb_client.get_rotten_tomato_rating(sys.argv[1]))

