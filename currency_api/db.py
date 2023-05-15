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

    @staticmethod
    def get_currency_json():
        return requests.get(f"https://api.currencyapi.com/v3/latest?apikey={Config.CURRENCY_API_TOKEN}").json()

    def set_currency(self):
        currency_object = self.get_currency_json()

        self.redis.json().set("data", '$', currency_object["data"])

    def get_currency(self):
        return self.redis.json().get("data")

    def get_currency_to_convert(self, currency_from, currency_to):
        currency_from_value = self.redis.json().get("data", Path(f".{currency_from}"))
        currency_to_value = self.redis.json().get("data", Path(f".{currency_to}"))

        return currency_from_value, currency_to_value

    def merge(self, merge_num=0):
        currency_object = self.get_currency_json()

        if merge_num == 0:
            if self.redis.exists("data"):
                self.redis.json().delete("data")
                self.redis.json().set("data", '$', currency_object["data"])
        else:
            pass
