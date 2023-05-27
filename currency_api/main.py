from contextvars import ContextVar
from aiohttp import web

from .handlers import Handler
from .routes import setup_routes
from .db import Redis

from config import Config


VAR = ContextVar("VAR", default="default")
REDIS = Redis()


async def on_startup(app):
    REDIS.start_up(
        host=Config.HOST,
        port=Config.PORT,
        db=0,
        password=Config.PASSWORD,
        charset="utf-8",
        decode_responses=True
    )
    setup_routes(app, Handler, REDIS)


async def on_shut_down(app):
    REDIS.shut_down()


def init_func(argv):
    app = web.Application()
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shut_down)
    return app


# if __name__ == "__main__":
#     app = init_func(argv)
#     web.run_app(app)
