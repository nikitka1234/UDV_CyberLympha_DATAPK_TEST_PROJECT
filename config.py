import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    PASSWORD = os.getenv("PASSWORD")

    CURRENCY_API_TOKEN = os.getenv("CURRENCY_API_TOKEN")
