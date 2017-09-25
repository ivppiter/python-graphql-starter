# pylint: disable=C0111
import asyncio
import graphene

class BasicMutation(graphene.Mutation):
    value = graphene.String()

    async def mutate(self, info):
        await asyncio.sleep(2)
        return BasicMutation(value='mutation complete')
