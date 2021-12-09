# Cisco_Interview

Steps that need to be done to get Rotten Tomatoes rating for given movie title:
  0. Fill OMDB_KEY variable in .env file with your OMDB API key (can me obtain here: https://www.omdbapi.com/apikey.aspx)
  1. Build docker image: docker build -t=omdb_image <Dockerfile path>
  2. Run a container based on omdb_image: docker run --name omdb_container omdb_image
  3. Execute command to run get_omdb_movie.py script: docker exec -it omdb_container python get_omdb_movie.py <movie title in quotes>
 
  Example: docker exec -it cisco python get_omdb_movie.py "Guardians of the Galaxy Vol. 2"
  
