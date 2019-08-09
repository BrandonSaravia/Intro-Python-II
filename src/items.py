class Items:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        s = f'Item Name: {self.name}\nDescription: {self.description}'
        return s

    def __repr__(self):
        return f'Room({repr(self.name)}, {repr(self.description)})'


    