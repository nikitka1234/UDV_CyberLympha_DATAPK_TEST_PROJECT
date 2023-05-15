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

        currency_from, currency_to = self.redis.get_currency_to_convert(currency_from, currency_to)

        per = currency_amount / currency_from["value"]
        res = currency_to["value"] * per

        return web.json_response({"data": {
            f"from {currency_from['code']}": currency_from,
            f"to {currency_to['code']}": currency_to,
            "result": {"value": round(res, 1), "percent": round(per, 1)}
        }})

    async def database(self, request):
        merge = int(request.rel_url.query.get("merge"))
        self.redis.merge(merge)
        return web.json_response(self.redis.get_currency_json())
