FROM python:3.9-alpine

WORKDIR /usr/src/app

COPY get_omdb_movie.py ./
COPY omdb_client.py ./
COPY requirements.txt ./
COPY .env ./

RUN pip install -r requirements.txt

ENTRYPOINT ["tail"]
CMD ["-f", "/dev/null"]
