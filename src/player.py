# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        s = f'Player Name: {self.name}\nCurrent location: {self.current_room}'
        return s

    def __repr__(self):
        return f'Room({repr(self.name)}, {repr(self.current_Room_Location)}, {repr(self.starting_Room)})'

    