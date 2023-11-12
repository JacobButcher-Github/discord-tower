from discord import Client
from random import randint
from initiative import Initiative


class TowerClient(Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        self.reset()
    

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
                    
                    case 'density':
                        res = self.density_handler(args)
                    
                    case 'turn':
                        res = self.turn_handler(args)

                    case 'caco':
                        res = self.caco_handler(args)

                    case 'crit': 
                        res = self.calc_crit(args)

                    case 'initiative':
                        res = self.init_handler(args)

                    case 'reset':
                        res = self.reset()
            
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
            ".tower batcon -> prints current battle condition\n\n" +

            ".tower density rules -> prints density rules from TCR (my beloved)\n" +
            ".tower density set [Number] -> Sets current density to number\n" +
            ".tower density add [Number] -> Adds number to current density\n" +
            ".tower density sub [Number] -> Subtracts number from current density\n" +
            ".tower density -> Displays current Shinsu Density\n\n" +

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
            ".tower initiative -> give list of players in queue" +
            ".tower initiative list -> give list of all players" +
            ".tower initiative remove [Name] -> Removes a person from queue (If ko'd, for instance)\n\n" +

            ".tower reset -> resets all fields"
        )

        return res


    def stats(self, args):
        res = 'invalid stats'

        match len(args):
            case 2:
                if self.boss_stats:
                    res = self.boss_stats
                else:
                    res = 'boss stats not set'
            
            case 7 | 8:
                if args[2] == 'set':
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
                        
                        res = 'stats set'
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
    

    def density_handler(self, args):
        res = 'invalid density'

        match len(args):
            case 2:
                if self.density:
                    res = f'{self.density} density'
                else:
                    res = 'density not set'
            
            case 3:
                if args[2] == 'rules':
                    res = (
                        'In certain areas within the Tower, characters may encounter areas with high shinsu density. ' +
                        'These areas become more and more common the further up the Tower a character goes. ' +
                        'When shinsu density reaches certain levels, various effects will be applied to all entities within that area. ' +
                        'All effects of lower levels of shinsu density are also applied at a higher level of shinsu density. ' +
                        'At the end of each turn, if a character in an area with high shinsu density has lost shinsu, ' +
                        'they can absorb 10 shinsu from the area and lower the level of shinsu density by 1, then that character regains 10 shinsu.\n\n' +

                        'Characters which have a skill named "Shinsu Resistance" are unaffected by the effects of shinsu density at levels equal ' +
                        'to or less than their shinsu resistance level.\n\n' +

                        'Level 5 - Characters lose hp equal to the shinsu density level at the end of each turn\n' +
                        'Level 10 - Weapons that are not needles, swords, spears, and hooks deal halved damage\n' +
                        'Level 15 - Characters lose the ability to take positions\n' +
                        'Level 20 - Magical skills are treated as though 10 less shinsu was used on them\n' +
                        'Level 25 - Characters lose attack and speed equal to the shinsu density level\n' +
                        'Level 30 - Weapons and items that are not needles, swords, spears, and hooks deal 0 damage and cease to function\n' +
                        'Level 40 - Environmental effects are negated, magical skills are treated as though 30 less shinsu was used on them, ' +
                        'and physical attacks and skills deal halved damage\n' +
                        'Level 50 - All entities lose the ability to move and take action'
                    )

            case 4:
                try:
                    num = int(args[3])

                    match args[2]:
                        case 'set':
                            self.density = num
                            res = f'density set to {self.density}'
                            
                        case 'add':
                            self.density += num
                            res = f'density raised to {self.density}'

                        case 'sub':
                            self.density = max(0, self.density - num)
                            res = f'density lowered to {self.density}'
                except:
                    pass
        
        return res
    

    def turn_handler(self, args):
        res = 'invalid turn'

        match len(args):
            case 2:
                if self.turn:
                    res = f'Turn {self.turn}'
                else:
                    res = 'turn not set'

            case 4:
                try:
                    num = int(args[3])

                    match args[2]:
                        case 'set':
                            self.turn = num
                            res = f'turn set to {self.turn}'
                            
                        case 'add':
                            self.turn += num
                            self.roll_for.next_turn()
                            res = f'turn moved to {self.turn}'

                        case 'sub':
                            self.turn = max(0, self.turn - num)
                            res = f'turn reverted to {self.turn}'
                except:
                    pass
        
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


    def init_handler(self, args):
        res = "Error"

        if (len(args) == 2):
            res = self.roll_for.display_queue()
            return res
        
        if (len(args) == 3 and args[3] == "list"):
            res = self.roll_for.display_list()
            return res

        if (len(args) == 3 and args[2] == "next"):
            res = self.roll_for.next_player()
            return res
        
        elif(len(args) == 5 and args[2] == "add"):
            res = f"{args[3]} added"
            self.roll_for.add_player(args[3], int(args[4]))
            return res
        
        elif(len(args) == 5 and args[2] == "update"):
            res = f"{args[3]} updated"
            self.roll_for.update_player(args[3], int(args[4]))
            return res
        
        elif(len(args) == 4 and args[2] == "remove"):
            res = f"{args[3]} removed"
            self.roll_for.remove_player(args[3])
            return res
        
        return res


    def reset(self):
        # State variables
        self.boss_stats = ''
        self.boss_hp = 0
        self.batcon = ''
        self.density = 0
        self.turn = 0
        self.caco = 0
        self.roll_for = Initiative()

        return 'all fields reset'
