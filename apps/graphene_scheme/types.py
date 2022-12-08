from graphene_django.types import DjangoObjectType

from apps.movies.models import Category, Movie


class CategoryType(DjangoObjectType):

    class Meta:
        model = Category


class MovieType(DjangoObjectType):

    class Meta:
        model = Movie
