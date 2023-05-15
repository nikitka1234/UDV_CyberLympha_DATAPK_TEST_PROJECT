from aiohttp import web


class Handler:
    def __init__(self, redis):
        self.redis = redis

    @staticmethod
    async def hello(request):
        return web.Response(text="Hello, world")

    async def convert(self, request):
        currency_from = request.rel_url.query.get("from", "RUB")
        currency_to = request.rel_url.query.get("to", "USD")
        currency_amount = int(request.rel_url.query.get("amount", 10))

        currency_from, currency_to = self.redis.get_currency(currency_from, currency_to)

        per = currency_amount / currency_from["value"]
        res = currency_to["value"] * per

        return web.Response(text=f"{currency_from}, {currency_to}, {currency_amount}, {res}")

    async def database(self, request):
        merge = request.rel_url.query.get("merge")
