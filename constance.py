from enum import Enum

TOKEN_FILE = "token.txt"

# Model
STAT_ORDER = ("atk", "hp", "spd", "shi")
STATS = set(
    [
        "atk",
        "hp",
        "spd",
        "shi",
        "cry",
        "psi",
        "ki",
        "unk",
        "tra",
        "obv",
        "eld",
        "com",
        "eth",
        # These are cursed
        "cor",
        "dig",
        "cho",
    ]
)
FX = set(
    [
        "dr",
        "dr%",
    ]
)
BUFFS = set(
    [
        "dr",
        "dr%",
        "buff",
    ]
)


class DamageType(Enum):
    PHYSICAL = ("physical", False)
    PHYSICAL_PIERCING = ("physical", True)
    MAGICAL = ("magical", False)
    MAGICAL_PIERCING = ("magical", True)
    TRUE = ("true", False)

    def __init__(self, base_type: str, piercing: bool):
        self._base_type = base_type
        self._piercing = piercing

    @property
    def base_type(self):
        return self._base_type

    @property
    def is_piercing(self):
        return self._piercing


# Limits (for Urban)
MAX_ROLLS = 100
MAX_SIDES = 1000

# Help Command
HELP1 = (
    ".tower stats set [atk] [hp] [spd] [shi] [???] -> Sets current boss to these stats\n"
    + ".tower stats -> return stats of current boss\n\n"
    + ".tower hp set [Number] -> Sets current boss to this hp\n"
    + ".tower hp add [Number] -> Adds number to  current boss hp\n"
    + ".tower hp sub [Number] -> Subtracts number from current boss hp\n"
    + ".tower hp -> Prints current boss hp\n\n"
    + ".tower turn set [Number] -> Set current turn to number\n"
    + ".tower turn add [Number] -> Adds number to current turn\n"
    + ".tower turn sub [Number] -> Subtracts number from current turn\n"
    + ".tower turn -> Displays current turn"
)

HELP2 = (
    ".tower batcon set [String]-> Sets current battle condition\n"
    + ".tower batcon -> prints current battle condition\n\n"
    + ".tower density rules -> prints density rules from TCR (my beloved)\n"
    + ".tower density set [Number] -> Sets current density to number\n"
    + ".tower density add [Number] -> Adds number to current density\n"
    + ".tower density sub [Number] -> Subtracts number from current density\n"
    + ".tower density -> Displays current Shinsu Density"
)

HELP3 = (
    ".tower caco -> Gives current value of caco\n"
    + ".tower caco set [Number] -> Set current caco atk value to number\n"
    + ".tower caco add [Number] -> Add number to current caco atk value\n"
    + ".tower caco sub [Number] -> Subtract number from current caco atk value\n\n"
    + ".tower crit [chance] [damage of move] [# of times used] -> Calculates the damage complete with crit\n"
    + ".tower roll [optional number (max 100)]d[sides (max 1000)]"
)

HELP4 = (
    ".tower initiative add [Name] [Priority Speed] -> Prepares person in the queue\n"
    + ".tower initiative update [Name] [New Priority Speed] -> Updates person in queue\n"
    + ".tower initiative next -> Gives next person in the priority queue\n"
    + ".tower initiative -> give list of players in queue\n"
    + ".tower initiative list -> give list of all players\n"
    + ".tower initiative remove [Name] -> Removes a person from queue (If ko'd, for instance)\n\n"
    + ".tower reset -> resets all fields"
)

DENSITY = (
    "In certain areas within the Tower, characters may encounter areas with high shinsu density. "
    + "These areas become more and more common the further up the Tower a character goes. "
    + "When shinsu density reaches certain levels, various effects will be applied to all entities within that area. "
    + "All effects of lower levels of shinsu density are also applied at a higher level of shinsu density. "
    + "At the end of each turn, if a character in an area with high shinsu density has lost shinsu, "
    + "they can absorb 10 shinsu from the area and lower the level of shinsu density by 1, then that character regains 10 shinsu.\n\n"
    + 'Characters which have a skill named "Shinsu Resistance" are unaffected by the effects of shinsu density at levels equal '
    + "to or less than their shinsu resistance level.\n\n"
    + "Level 5 - Characters lose hp equal to the shinsu density level at the end of each turn\n"
    + "Level 10 - Weapons that are not needles, swords, spears, and hooks deal halved damage\n"
    + "Level 15 - Characters lose the ability to take positions\n"
    + "Level 20 - Magical skills are treated as though 10 less shinsu was used on them\n"
    + "Level 25 - Characters lose attack and speed equal to the shinsu density level\n"
    + "Level 30 - Weapons and items that are not needles, swords, spears, and hooks deal 0 damage and cease to function\n"
    + "Level 40 - Environmental effects are negated, magical skills are treated as though 30 less shinsu was used on them, "
    + "and physical attacks and skills deal halved damage\n"
    + "Level 50 - All entities lose the ability to move and take action"
)

# Media
LTG = "https://tenor.com/view/low-tier-god-ltg-gif-24660602"
TCR = "<https://drmmo.proboards.com/thread/6403/tower-comprehensive-rules>\nhttps://media.discordapp.net/attachments/245589536845856777/1111426152096071760/makesweet-ghv12k.gif?ex=65a070c3&is=658dfbc3&hm=25dd2c292fae849b2a832804759a5b43aae9e016c3913829f5826de693e3dab6&"
KERTA = "Kerta🧍‍♂️40,000 HP ❤️8000 atk💪7500 spd 🏃Unresistable 🚫 Statuses blood field 🩸30 stacks every action 🎬Reactive Grab 🤝 that heals him 💗8000 targeted AoE 🌋 hybrid ☯️Cooldown is only ☝️ turn too 🕐Instant attack and move action per 10 bleeding ‼️ Sets attack, speed, shinsu to 0️⃣ when grabbed with Honden's🧙‍♂️ Chains ⛓️ + sealed 🔒. Multi ranged 🎯grab with it too! Has alligators 🐊 he didn't even use!"
