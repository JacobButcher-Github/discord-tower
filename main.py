from discord import Intents
from tower_bot import TowerClient


if __name__ == '__main__':
    token: str = open('token.txt').read()

    intents: Intents = Intents.default()
    intents.message_content = True

    client: TowerClient = TowerClient(intents=intents)
    client.run(token)
