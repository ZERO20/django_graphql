import graphene

from apps.graphene_scheme.query import Query as SchemeQuery
from apps.graphene_scheme.mutation import Mutation as SchemeMutation


class Query(SchemeQuery, graphene.ObjectType):
    pass


class Mutation(SchemeMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
