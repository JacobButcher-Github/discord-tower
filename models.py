from constance import *


class Character:
    def __init__(self, name: str, base_stats: dict, extra_stats: dict = None):
        self.name = name
        self.base_stats = base_stats
        self.extra_stats = extra_stats

        self.cur_stats = base_stats.copy()
        self.cur_extra_stats = extra_stats.copy() if extra_stats else None

        '''
        {
            <effect>: {
                'timer': <turns>,
                <affected_stat>: <tick_amount>,
            },
        }
        '''
        self.effects = {}


    # Name - #atk/#hp/#spd/#shi/...(/...)
    def get_stats(self, base: bool = False) -> str:
        stats = self.base_stats if base else self.cur_stats
        extra_stats = self.extra_stats if base else self.cur_extra_stats

        stat_str = f'{self.name} - '

        for stat in STAT_ORDER:
            if stat in stats:
                stat_str += f'{stats[stat]}{stat}/'

        for stat in stats:
            if stat not in STAT_ORDER:
                stat_str += f'{stats[stat]}{stat}/'

        stat_str = stat_str[:-1]

        if extra_stats:
            stat_str += '('

            for stat in extra_stats:
                stat_str += f'/{extra_stats[stat]}{stat}'

            stat_str += ')'

        return stat_str


    def mod_stats(self, stat: str, diff: int) -> None:
        tar = None

        if stat in self.cur_stats:
            tar = self.cur_stats
        elif stat in self.cur_extra_stats:
            tar = self.cur_extra_stats

        if tar and type(tar[stat]) is not str:
            tar[stat] += diff


    def damage(self, amount: int) -> None:
        # dmg amp
        if 'vuln' in self.effects:
            amount += self.effects['vuln']

        if 'vuln%' in self.effects:
            amount *= self.effects['vuln%']

        # TODO: damage types

        # dmg reduc
        if 'dr%' in self.effects:
            amount = int(amount * self.effects['dr%'])

        if 'dr' in self.effects:
            amount = max(0, amount - self.effects['dr'])

        if self.cur_stats['hp'] > 0:
            self.cur_stats['hp'] = max(0, self.cur_stats['hp'] - amount)
        else:
            self.cur_stats['hp'] -= amount


    def heal(self, amount: int) -> None:
        self.cur_stats['hp'] = min(self.base_stats['hp'], self.cur_stats['hp'] + amount)


    def turn_tick(self, turn: int) -> None:
        for effect in self.effects:
            pass
