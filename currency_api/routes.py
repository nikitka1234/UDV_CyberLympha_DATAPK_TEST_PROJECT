def setup_routes(app, handler, redis):
    router = app.router
    handler = handler(redis)
    router.add_get('/', handler.hello, name='hello')
    router.add_get('/convert', handler.convert, name='convert')
    router.add_post('/database', handler.database, name='database')
