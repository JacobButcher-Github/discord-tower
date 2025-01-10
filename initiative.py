from collections import deque


class Initiative:
    def __init__(self):
        self.goingnext: deque[str] = deque()
        self.player_list: list[dict[str, int | str]] = []
        # Used exclusively exists in case someone new shows up in the middle of the fight
        self.used: set[str] = set()
        self.exists: set[str] = set()

    def set_queue(self):
        self.player_list.sort(key=lambda x: x["prio"])
        self.goingnext = deque()

        for i in self.player_list:
            if i["name"] not in self.used and isinstance(i["name"], str):
                self.goingnext.append(i["name"])

    def add_player(self, name: str, prio: int):
        self.player_list.append({"name": name, "prio": prio})
        self.exists.add(name)
        self.set_queue()

    def update_player(self, name: str, prio: int):
        for i in self.player_list:
            if i["name"] == name:
                i["prio"] = prio
                break
        self.set_queue()

    def remove_player(self, name: str):
        for i in self.player_list:
            if i["name"] == name:
                self.player_list.remove(i)
                break
        self.set_queue()

    def next_player(self):
        next = self.goingnext.pop()
        self.used.add(next)
        return next

    def next_turn(self):
        self.used = set()

    def display_list(self):
        res = ""

        for i in self.player_list[::-1]:
            res += f"{i["name"]}: {i["prio"]}\n"
        return res

    def display_queue(self):
        return "\n".join(self.goingnext)
