import graphene

from products.schema import Query as ProductQuery
from events.schema import Query as EventQuery


class Query(ProductQuery, EventQuery):
    pass


schema = graphene.Schema(query=Query)
