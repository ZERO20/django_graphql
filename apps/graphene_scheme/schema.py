import graphene

from apps.graphene_scheme.query import Query as SchemeQuery


class Query(SchemeQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
