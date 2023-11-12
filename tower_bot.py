from discord import *
from random import randint


class TowerClient(Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

        # State variables
        self.density = 0
    

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        txt = message.content.lower()

        if txt.startswith('.tower'):
            res = 'from tower?' # Default response
            args = txt.split()

            if len(args) > 1:
                match args[1]:
                    case 'crit': 
                        res = self.calc_crit(args)
            
            await message.channel.send(res)
    

    def calc_crit(self, args):
        # .tower crit [chance] [damage of move] [# of times used]
        res = 'invalid crit'

        if len(args) == 5:
            try:
                chance = int(args[2])
                dmg = int(args[3])
                times = int(args[4])

                crit_dmg = dmg * times * (2 ** self.roll_success(chance))
                res = f'crit for {crit_dmg}'
            except:
                pass
        
        return res


    def roll_success(self, percent):
        success = percent // 100
        percent %= 100

        if randint(1, 100) <= percent:
            success += 1

        return success
