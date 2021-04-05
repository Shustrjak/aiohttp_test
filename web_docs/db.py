# import asyncio

import aiopg.sa
import sqlalchemy as sa



meta = sa.MetaData()

table_documents = sa.Table(
    'documents', meta,
    sa.Column('id', sa.Integer, primary_key=True, unique=True, autoincrement=True),
    sa.Column('name', sa.String(200), nullable=True),
    sa.Column('created', sa.Date, nullable=True),
    sa.Column('updated', sa.Date, nullable=True)
)


async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
            database=conf['database'],
            user=conf['user'],
            password=conf['password'],
            host=conf['host'],
            port=conf['port'],
            minsize=conf['minsize'],
            maxsize=conf['maxsize'],
    )
    app['documents'] = engine


async def close_pg(app):
    app['documents'].close()
    await app['documents'].wait_closed()
