from apps.movies.models import Movie, Director, Actor
from rest_framework import serializers


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        movie_title = validated_data.get('title')
        release_year = validated_data.get('release_year')

        existing_movie = Movie.objects.filter(title=movie_title, release_year=release_year).first()
        if existing_movie:
            return existing_movie

        director_data = validated_data.pop('director')
        actors_data = validated_data.pop('actors')

        director, created_director = Director.objects.get_or_create(**director_data)
        actors = [Actor.objects.get_or_create(**actor_data)[0] for actor_data in actors_data]

        movie = Movie.objects.create(director=director, **validated_data)
        movie.actors.set(actors)

        return movie

    def update(self, instance, validated_data):
        if 'director' in validated_data:
            director_data = validated_data.pop('director')
            director, created = Director.objects.get_or_create(name=director_data.get('name'))
            instance.director = director

        if 'actors' in validated_data:
            actors_data = validated_data.pop('actors')
            updated_actors = []
            for actor_data in actors_data:
                actor, created = Actor.objects.get_or_create(name=actor_data.get('name'))
                updated_actors.append(actor)
            instance.actors.set(updated_actors)

        instance.title = validated_data.get('title', instance.title)
        instance.release_year = validated_data.get('release_year', instance.release_year)
        instance.save()

        return instance
