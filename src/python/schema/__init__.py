# pylint: disable=C0111
import asyncio
import graphene
from .mutations import BasicMutation

async def resolve_async_value(root, info, name):
    print('Argument {}', info)
    await asyncio.sleep(2)
    return 'Hello {}!'.format(name)

class Query(graphene.ObjectType):
    hello = graphene.String()
    async_value = graphene.String(name=graphene.String(required=True), resolver=resolve_async_value)

    def resolve_hello(self, info):
        return 'world'

class Mutation(graphene.ObjectType):
    basic_mutation = BasicMutation.Field()
