import graphene

import products.schema
import events.schema


class Query(products.schema.Query, events.schema.Query):
    pass


class Mutation(products.schema.Mutation, events.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
