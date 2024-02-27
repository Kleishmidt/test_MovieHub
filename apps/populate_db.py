import os
import sys

import django

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.utils import fetch_movie_data


def populate_movies():
    movie_titles = [
        'Interstellar',
        'Inception',
        'The Shawshank Redemption',
        'The Dark Knight',
        'Back to the Future',
        'Pulp Fiction',
        'Forrest Gump',
        'The Godfather',
        'The Green Mile',
        'Goodfellas',
    ]
    for title in movie_titles:
        movie = fetch_movie_data(title)
        if movie:
            print(f"Added movie: {movie}")


if __name__ == '__main__':
    populate_movies()
