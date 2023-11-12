from collections import deque

class Initiative:
    def __init__(self):
        self.goingnext = deque()
        self.player_list = list()
        self.used = set()


    def set_queue(self):
        self.player_list.sort(key = lambda x: x[0])

        for i in self.player_list:
            if i[1] not in self.used:
                self.goingnext.append(i[1])
        

    def add_player(self, name, prio):
        self.player_list.append((prio, name))
        self.set_queue()


    def update_player(self, name, prio):
        for i in self.player_list:
            if (i[1] == name):
                i[0] = prio
                break
        self.setqueue()
    

    def remove_player(self, name):
        for i in self.player_list:
            if (i[1] == name):
                self.player_list.pop(i)
                break
        self.setqueue()


    def next_player(self):
        next = self.goingnext.pop()
        self.used.add(next)
        return next
    
    def next_turn(self):
        self.used = set()

    def display_list(self):
        res = ""
        for i in self.player_list:
            res += (f"{i[1]}: {i[0]}\n")
        return res
    
    def display_queue(self):
        res = ""
        for i in self.goingnext:
            res += "i\n"
        return res
