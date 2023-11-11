from discord import *


class TowerClient(Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
    

    async def on_message(self, message):
        if message.author == self.user:
            return

        txt = message.content.lower()

        if txt.startswith('.tower'):
            args = txt.split()
            res = 'from tower?'

            if len(args) > 1:
                match args[1]:
                    case "crit": # .tower crit [chance] [damage of move] [#of times used]
                        if len(args) == 5:
                            res = 'valid crit'
            
            await message.channel.send(res)
