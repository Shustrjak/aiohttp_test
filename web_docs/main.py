import asyncio
import sys

from aiohttp import web

from web_docs.db import init_pg, close_pg
from web_docs.routes import setup_routes
from web_docs.settings import config

app = web.Application()
setup_routes(app)
app['config'] = config

app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)

if __name__ == '__main__':
    if sys.version_info >= (3, 8) and sys.platform.lower().startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    web.run_app(app, host='127.0.0.1')
