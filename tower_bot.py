from discord import *
from random import randint


class TowerClient(Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

        # State variables
        self.stats = ""
        self.hp = 0

        self.batcon = ""
        self.density = 0

        self.caco = 0
    

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        txt = message.content.lower()

        if txt.startswith('.tower'):
            res = 'from tower? .tower help for list of commands.' # Default response
            args = txt.split()

            if len(args) > 1:
                match args[1]:
                    case 'help':
                        res = self.help_text()
                    
                    case 'stats':
                        res = self.stats(args)

                    case 'crit': 
                        res = self.calc_crit(args)
            
            await message.channel.send(res)
    

    def help_text(self):
        res = (
                ".tower stats set [atk] [hp] [spd] [shi] [???] -> Sets current boss to these stats\n" +
                ".tower stats -> return stats of current boss\n\n" +

                ".tower hp set -> Sets current boss to this hp\n" +
                ".tower hp add [Number] -> Adds number to  current boss hp\n" +
                ".tower hp sub [Number] -> Subtracts number from current boss hp\n" +
                ".tower hp -> Prints current boss hp\n\n" +

                ".tower batcon set [String]-> Sets current battle condition\n" +
                ".tower batcon -> prints current battle condition\n" +

                ".tower density rules -> prints density rules from TCR (my beloved)\n" +
                ".tower density set [Number] -> Sets current density to number\n" +
                ".tower density add [Number] -> Adds number to current density\n" +
                ".tower density sub [Number] -> Subtracts number from current density\n" +
                ".tower density -> Displays current Shinsu Density" +
                
                ""
        )

        return res


    def stats(args):
        pass


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
