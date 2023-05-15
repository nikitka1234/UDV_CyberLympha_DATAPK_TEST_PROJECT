from aiohttp import web

from .handlers import Handler
from .routes import setup_routes
from .db import Redis

from config import Config


def init_func(argv):
    app = web.Application()
    redis = Redis(
        host=Config.HOST,
        port=Config.PORT,
        db=0,
        password=Config.PASSWORD,
        charset="utf-8",
        decode_responses=True
    )
    setup_routes(app, Handler, redis)
    return app


# if __name__ == "__main__":
#     app = init_func(argv)
#     web.run_app(app)
