from discord import Intents
from tower_bot import TowerClient


if __name__ == '__main__':
    token = open('token.txt').read()

    intents = Intents.default()
    intents.message_content = True

    client = TowerClient(intents=intents)
    client.run(token)
