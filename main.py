from discord import Intents, Interaction, app_commands

from commands import register_commands
from tower_bot import TowerClient

if __name__ == "__main__":
    token: str = open("token.txt").read()

    intents: Intents = Intents.default()
    intents.message_content = True

    client: TowerClient = TowerClient(intents=intents)
    register_commands(client.tree)

    client.run(token)
