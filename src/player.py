# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    
    def __init__(self, name, current_room, playerclass, items=[]):
        self.name = name
        self.playerclass = playerclass
        self.current_room = current_room
        self.items = items

    def __str__(self):
        s = f'Player Name: {self.name}\n{self.current_room}\nClass: {self.playerclass}'
        return s

    def __repr__(self):
        return f'Room({repr(self.name)}, {repr(self.current_Room_Location)}, {repr(self.starting_Room)})'

    