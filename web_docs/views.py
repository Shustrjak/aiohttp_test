import datetime

from aiohttp import web

from . import db


async def index(request):
    async with request.app['documents'].acquire() as conn:
        cursor = await conn.execute(db.table_documents.select())
        records = await cursor.fetchall()
        documents = [dict(q) for q in records]
        return web.Response(text=str(documents))


async def docs_post(request):
    async with request.app['documents'].acquire() as conn:
        data = {'id': '7',
                'name': 'name_doc_32',
                'created': f'{datetime.datetime.now()}',
                'updated': f'2020-10-19'}
        cursor = await conn.execute(db.table_documents.insert(), [data])
        cursor.close()
        cursor = await conn.execute(db.table_documents.select())
        records = await cursor.fetchall()
        documents = [dict(q) for q in records]
        return web.Response(text=str(documents))


async def docs_update(request):
    async with request.app['documents'].acquire() as conn:
        data = {'id': '48',
                'name': 'name_doc_32',
                'created': '2020-03-18 00:00:00',
                'updated': f'{datetime.datetime.now()}'}
        cursor = await conn.execute(db.table_documents.update().where(
            db.table_documents.c.updated == f'{datetime.datetime.now()}').returning(
            db.table_documents.c.name, db.table_documents.c.updated), data)
        cursor.close()
        cursor = await conn.execute(db.table_documents.select())
        records = await cursor.fetchall()
        documents = [dict(q) for q in records]
        return web.Response(text=str(documents))


async def docs_delete(request):
    async with request.app['documents'].acquire() as conn:
        cursor = await conn.execute(
            db.table_documents.delete().where(db.table_documents.c.id == '45'))
        cursor.close()
        cursor = await conn.execute(db.table_documents.select())
        records = await cursor.fetchall()
        documents = [dict(q) for q in records]
        return web.Response(text=str(documents))
