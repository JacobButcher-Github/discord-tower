from discord import *


class MyClient(Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
    

    async def on_message(self, message):
        print(f'{message.author}: {message.content}')


def setup():
    token = open('token.txt').read()

    intents = Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)
    client.run(token)


if __name__ == '__main__':
    setup()
