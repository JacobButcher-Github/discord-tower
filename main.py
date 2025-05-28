from discord import Intents
from tower_bot import TowerClient
import constance as fedralis


if __name__ == '__main__':
    token: str = open(fedralis.TOKEN_FILE).read()

    intents: Intents = Intents.default()
    intents.message_content = True

    client: TowerClient = TowerClient(intents=intents)
    client.run(token)
