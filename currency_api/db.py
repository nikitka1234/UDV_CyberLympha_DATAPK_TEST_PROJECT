import redis
from redis.commands.json.path import Path
from config import Config

import requests


class Redis:
    def __init__(self, host='localhost', port=6379, db=0, password=None,
                 charset="utf-8", decode_responses=None):
        self.redis = redis.StrictRedis(
            host=host,
            port=port,
            db=db,
            password=password,
            charset=charset,
            decode_responses=decode_responses
        )

        self.redis.flushdb()
        self.set_currency()

    def set_currency(self):
        currency_object = requests.get(f"https://api.currencyapi.com/v3/latest?apikey={Config.CURRENCY_API_TOKEN}").json()

        self.redis.json().set("data", '$', currency_object["data"])

    def get_currency(self, currency_from, currency_to):
        currency_from_value = self.redis.json().get("data", Path(f".{currency_from}"))
        currency_to_value = self.redis.json().get("data", Path(f".{currency_to}"))

        return currency_from_value, currency_to_value

    def merge(self, num):
        pass
