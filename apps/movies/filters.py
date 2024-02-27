from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from apps.movies.models import Movie


class MovieFilter(FilterSet):
    director = CharFilter(field_name='director__name', lookup_expr='icontains')
    actor = CharFilter(field_name='actors__name', lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['release_year', 'director', 'actor']
