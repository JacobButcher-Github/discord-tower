from discord import *


class TowerClient(Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
    

    async def on_message(self, message):
        print(f'{message.author}: {message.content}')

        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')
