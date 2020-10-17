import logging
import os

from .bot import Janelle

logging.basicConfig(level=logging.INFO)
bot = Janelle()


def main() -> None:
    token = os.getenv("TOKEN")
    if token is None:
        print("Please provide a TOKEN enviroment variable")
        exit(1)

    bot.run(token)
