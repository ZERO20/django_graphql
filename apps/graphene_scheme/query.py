import graphene

from apps.movies.models import Category, Movie
from apps.graphene_scheme.types import CategoryType, MovieType


class Query(object):
    movie = graphene.Field(MovieType, id=graphene.Int(), name=graphene.String())
    all_categories = graphene.List(CategoryType)
    all_movies = graphene.List(MovieType)

    def resolve_all_categories(self, info, **kwargs):
        """Gets all categories"""
        return Category.objects.all()

    def resolve_all_movies(self, info, **kwargs):
        """Gets all movies"""
        return Movie.objects.select_related('category').all()

    def resolve_movie(self, info, **kwargs):
        """Gets a movie

        Args:
            info (_type_): _description_

        Returns:
            _type_: _description_
        """        """"""
        id = kwargs.get('id')
        name = kwargs.get('name')
        if id is not None:
            return Movie.objects.select_related('category').get(pk=id)
        if name is not None:
            return Movie.objects.select_related('category').get(name=name)
        return None
