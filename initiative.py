from collections import deque

class Initiative:
    def __init__(self):
        self.goingnext = deque()
        self.player_list = list()


    def set_queue(self):
        self.player_list.sort(key = lambda x: x[0])

        for i in self.player_list:
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
        return next
