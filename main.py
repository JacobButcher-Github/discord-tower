from discord import *
from tower_bot import *


if __name__ == '__main__':
    token = open('token.txt').read()

    intents = Intents.default()
    intents.message_content = True

    client = TowerClient(intents=intents)
    client.run(token)
