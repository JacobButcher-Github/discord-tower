from random import randint

from discord import Client, DMChannel, GroupChannel, Message

import constance
from initiative import Initiative


class TowerClient(Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")
        _ = self.reset()

    async def on_message(self, message: Message):
        if message.author == self.user or type(message.channel) in [
            DMChannel,
            GroupChannel,
        ]:
            return

        txt = message.content.lower()

        if txt.startswith(".tower"):
            print(f"{message.author} ({message.created_at}): {txt}")  # Logging purposes
            res = "from tower? .tower help for list of commands."  # Default response
            args = txt.split()

            if len(args) <= 1:
                return

            match args[1]:
                case "help":
                    res = self.help_text(args)

                case "stats":
                    res = self.stats(args)

                case "hp":
                    res = self.hp_handler(args)

                case "batcon":
                    res = self.batcon_handler(args)

                case "density":
                    res = self.density_handler(args)

                case "turn":
                    res = self.turn_handler(args)

                case "caco":
                    res = self.caco_handler(args)

                case "crit":
                    res = self.calc_crit(args)

                case "roll":
                    res = self.roll(args)

                case "initiative":
                    res = self.init_handler(args)

                case "reset":
                    res = self.reset()

                case "tcr":
                    res = self.tcr()

                case "kerta":
                    res = self.kerta()

            await message.channel.send(res)

    def help_text(self, args):
        res = ".tower help [1-4]"

        if len(args) == 3:
            match args[2]:
                case "1":
                    res = constance.HELP1

                case "2":
                    res = constance.HELP2

                case "3":
                    res = constance.HELP3

                case "4":
                    res = constance.HELP4

        return res

    def stats(self, args):
        res = "invalid stats"

        match len(args):
            case 2:
                if self.boss_stats:
                    res = self.boss_stats
                else:
                    res = "boss stats not set"

            case 7 | 8:
                if args[2] == "set":
                    try:
                        atk = int(args[3])
                        hp = int(args[4])
                        spd = int(args[5])
                        shi = int(args[6])

                        self.boss_stats = f"{atk}atk/{hp}hp/{spd}spd/{shi}shi"
                        self.boss_hp = hp

                        if len(args) == 8:
                            fifth = int(args[7])
                            self.boss_stats += f"/{fifth}???"

                        res = "stats set"
                    except:
                        pass

        return res

    def hp_handler(self, args):
        res = "Not Set"

        if len(args) == 2:
            if self.boss_hp == 0:
                return res
            else:
                res = f"Boss Hp: {self.boss_hp}"

        if len(args) == 4:
            if args[2] == "set":
                self.boss_hp = int(args[3])
                res = f"Set Boss Hp to: {self.boss_hp}"
            elif args[2] == "add":
                self.boss_hp += int(args[3])
                res = f"Boss Hp: {self.boss_hp}"
            elif args[2] == "sub":
                self.boss_hp -= int(args[3])
                res = f"Boss Hp: {self.boss_hp}"

        return res

    def batcon_handler(self, args):
        res = "Not Set"

        if len(args) == 2:
            if self.batcon != "":
                res = self.batcon

        if len(args) > 3 and args[2] == "set":
            res = ""
            for i in range(3, len(args)):
                res += args[i] + " "
                self.batcon = res

        return res

    def density_handler(self, args):
        res = "invalid density"

        match len(args):
            case 2:
                if self.density:
                    res = f"{self.density} density"
                else:
                    res = "density not set"

            case 3:
                if args[2] == "rules":
                    res = constance.DENSITY

            case 4:
                try:
                    num = int(args[3])

                    match args[2]:
                        case "set":
                            self.density = num
                            res = f"density set to {self.density}"

                        case "add":
                            self.density += num
                            res = f"density raised to {self.density}"

                        case "sub":
                            self.density = max(0, self.density - num)
                            res = f"density lowered to {self.density}"
                except:
                    pass

        return res

    def turn_handler(self, args):
        res = "invalid turn"

        match len(args):
            case 2:
                if self.turn:
                    res = f"Turn {self.turn}"
                else:
                    res = "turn not set"

            case 4:
                try:
                    num = int(args[3])

                    match args[2]:
                        case "set":
                            self.turn = num
                            res = f"turn set to {self.turn}"

                        case "add":
                            self.turn += num
                            self.roll_for.next_turn()
                            res = f"turn moved to {self.turn}"

                        case "sub":
                            self.turn = max(0, self.turn - num)
                            res = f"turn reverted to {self.turn}"
                except:
                    pass

        return res

    def caco_handler(self, args):
        res = "Not Set"

        if len(args) == 2:
            if self.caco == 0:
                return res
            else:
                res = f"Caco Atk: {self.caco}"

        if len(args) == 4:
            if args[2] == "set":
                self.caco = int(args[3])
                res = f"Caco Atk: {self.caco}"
            elif args[2] == "add":
                self.caco += int(args[3])
                res = f"Caco Atk: {self.caco}"
            elif args[2] == "sub":
                self.caco -= int(args[3])
                res = f"Caco Atk: {self.caco}"

        return res

    def calc_crit(self, args):
        res = "invalid crit"

        if len(args) == 5:
            try:
                chance = int(args[2])
                dmg = int(args[3])
                times = int(args[4])

                res = f"crit for"

                dmg_sum = 0

                for _ in range(times):
                    crit = dmg * (2 ** self.roll_success(chance))
                    res += f" {crit}"
                    dmg_sum += crit

                res += f" ({dmg_sum})"
            except:
                pass

        return res

    def roll(self, args: list[str]):
        res = "invalid roll"

        if len(args) != 3:
            return res

        try:
            if "d" in args[2]:
                s = args[2].split("d")

                if s[0]:
                    times = int(s[0])
                    dice = int(s[1])

                    if (
                        0 < times <= constance.MAX_ROLLS
                        and 0 < dice <= constance.MAX_SIDES
                    ):
                        rolls: list[int] = []

                        for _ in range(times):
                            rolls.append(randint(1, dice))

                        res = f"{sum(rolls)}\t|"

                        for roll in rolls:
                            res += f"\t{roll}"
                    else:
                        res = constance.LTG
                else:
                    die = int(s[1])

                    if 0 < die <= constance.MAX_SIDES:
                        res = f"{randint(1, die)}"
                    else:
                        res = constance.LTG
            else:
                die = int(args[2])

                if 0 < die <= constance.MAX_SIDES:
                    res = f"{randint(1, die)}"
                else:
                    res = constance.LTG
        except:
            pass

        return res

    def roll_success(self, percent: int):
        success = percent // 100
        percent %= 100

        if randint(1, 100) <= percent:
            success += 1

        return success

    def init_handler(self, args: list[str]):
        res = "Error"

        if len(args) == 2:
            res = self.roll_for.display_queue()
            return res if res else "empty"

        if len(args) == 3 and args[2] == "list":
            res = self.roll_for.display_list()
            return res if res else "empty"

        if len(args) == 3 and args[2] == "next":
            res = self.roll_for.next_player()
            return res

        elif len(args) == 5 and args[2] == "add":
            res = f"{args[3]} added"
            self.roll_for.add_player(args[3], int(args[4]))
            return res

        elif len(args) == 5 and args[2] == "update":
            res = f"{args[3]} updated"
            self.roll_for.update_player(args[3], int(args[4]))
            return res

        elif len(args) == 4 and args[2] == "remove":
            res = f"{args[3]} removed"
            self.roll_for.remove_player(args[3])
            return res

        return res

    def reset(self):
        # State variables
        self.boss_stats = ""
        self.boss_hp = 0
        self.batcon = ""
        self.density = 0
        self.turn = 0
        self.caco = 0
        self.roll_for = Initiative()

        return "All fields reset"

    def tcr(self):
        return constance.TCR

    def kerta(self):
        return constance.KERTA
