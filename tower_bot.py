from discord import *
from random import randint


class TowerClient(Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

        # State variables
        self.boss_stats = ""
        self.boss_hp = 0

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
                    
                    case 'hp':
                        res = self.hp_handler(args)
                    
                    case 'batcon':
                        res = self.batcon_handler(args)

                    case 'caco':
                        res = self.caco_handler(args)

                    case 'crit': 
                        res = self.calc_crit(args)
            
            await message.channel.send(res)
    

    def help_text(self):
        res = (
            ".tower stats set [atk] [hp] [spd] [shi] [???] -> Sets current boss to these stats\n" +
            ".tower stats -> return stats of current boss\n\n" +

            ".tower hp set [Number] -> Sets current boss to this hp\n" +
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

            ".tower turn set [Number] -> Set current turn to number\n" +
            ".tower turn add [Number] -> Adds number to current turn\n" +
            ".tower turn sub [Number] -> Subtracts number from current turn\n" +
            ".tower turn -> Displays current turn\n\n" +

            ".tower caco -> Gives current value of caco\n" +
            ".tower caco set [Number] -> Set current caco atk value to number\n" +
            ".tower caco add [Number] -> Add number to current caco atk value\n" +
            ".tower caco sub [Number] -> Subtract number from current caco atk value\n\n" +

            ".tower crit [chance] [damage of move] [# of times used] -> Calculates the damage complete with crit\n\n" +

            ".tower initiative add [Name] [Priority Speed] -> Prepares person in the queue\n" +
            ".tower initiative update [Name] [New Priority Speed] -> Updates person in queue\n" +
            ".tower initiative next -> Gives next person in the priority queue\n" +
            ".tower initiative remove [Name] -> Removes a person from queue (If ko'd, for instance)\n\n" +

            ".tower reset -> resets all fields"
        )

        return res


    def stats(self, args):
        res = "invalid stats"

        if len(args) == 2:
            if self.boss_stats:
                res = self.boss_stats
            else:
                res = "boss stats not set"
        elif len(args) in [7, 8]:
            if args[2] == "set":
                try:
                    atk = int(args[3])
                    hp = int(args[4])
                    spd = int(args[5])
                    shi = int(args[6])
                    
                    self.boss_stats = f'{atk}atk/{hp}hp/{spd}spd/{shi}shi'
                    self.boss_hp = hp

                    if len(args) == 8:
                        fifth = int(args[7])
                        self.boss_stats += f'/{fifth}???'
                    
                    res = "stats set"
                except:
                    pass

        return res


    def hp_handler(self, args):
        res = 'Not Set'

        if len(args) == 2:
            if (self.boss_hp == 0):
                return res
            else:
                res = f"Boss Hp: {self.boss_hp}"

        if len(args) == 4:
            if (args[2] == "set"):
                self.boss_hp = int(args[3])
                res = f"Set Boss Hp to: {self.boss_hp}"
            elif (args[2] == "add"):
                self.boss_hp += int(args[3])
                res = f"Boss Hp: {self.boss_hp}"
            elif (args[2] == "sub"):
                self.boss_hp -= int(args[3])
                res = f"Boss Hp: {self.boss_hp}"

        return res


    def batcon_handler(self, args):
        res = "Not Set"
        
        if (len(args) == 2):
            if (self.batcon != ""):
                res = self.batcon

        if (len(args) > 3 and args[2] == "set"):
            res = ""
            for i in range(3, len(args)):
                res += args[i]+" "
                self.batcon = res
    
        return res
    

    def caco_handler(self, args):
        res = 'Not Set'

        if len(args) == 2:
            if (self.caco == 0):
                return res
            else:
                res = f"Caco Atk: {self.caco}"

        if len(args) == 4:
            if (args[2] == "set"):
                self.caco = int(args[3])
                res = f"Caco Atk: {self.caco}"
            elif (args[2] == "add"):
                self.caco += int(args[3])
                res = f"Caco Atk: {self.caco}"
            elif (args[2] == "sub"):
                self.caco -= int(args[3])
                res = f"Caco Atk: {self.caco}"

        return res


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
