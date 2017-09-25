# pylint: disable=C0111
from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema
from graphql.execution.executors.asyncio import AsyncioExecutor
from schema import Query, Mutation

app = Flask(__name__)
app.secret_key = '3266ec32420f49b38d6fa78bde8cbe5f'
app.session_cookie_name = 'flasky-app'
app.debug = True
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=Schema(query=Query, mutation=Mutation),
        graphiql=True, # for having the GraphiQL interface
        executor=AsyncioExecutor()
    )
)

if __name__ == '__main__':
    app.run()
