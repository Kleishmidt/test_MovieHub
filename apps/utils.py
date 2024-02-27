import requests
from django.core.exceptions import ValidationError

from apps.movies.models import Movie, Actor, Director
from core.settings import OMDB_API_KEY


def fetch_movie_data(title):
    url = f'https://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={title}'
    response = requests.get(url)

    try:
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movie data: {e}")
        return None

    try:
        movie = create_movie_instance(data)
        return movie
    except (ValidationError, KeyError) as e:
        print(f"Error creating Movie instance: {e}")
        return None


def create_movie_instance(data):
    title = data.get('Title')
    release_year = int(data.get('Year'))

    existing_movie = Movie.objects.filter(title=title, release_year=release_year).first()

    if existing_movie:
        return existing_movie

    director_name = data.get('Director')
    actors_data = data.get('Actors').split(', ')

    director = Director.objects.get_or_create(name=director_name)[0]
    actors = [Actor.objects.get_or_create(name=actor)[0] for actor in actors_data]

    movie = Movie.objects.create(title=title, release_year=release_year, director=director)
    movie.actors.set(actors)

    return movie
