from room import Room
from player import Player
from items import Items
import random
import sys
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     Items('Blue_Scroll', "There's hyrogliphs on the scroll dipicting the Water")),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
Items('White_Scroll', "There's hyrogliphs on the scroll dipicting the Sky")),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
Items('Black_Scroll', "There's hyrogliphs on the scroll dipicting the Earth")),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Items

items = {
    'Blue_Scroll': Items('Blue_Scroll', "There's hyrogliphs on the scroll dipicting Water"),
    'Black_Scroll': Items('Black_Scroll', "There's hyrogliphs on the scroll dipicting Earth"),
    'White_Scroll': Items('White_Scroll', "There's hyrogliphs on the scroll dipicting the Sky"),
}


room['outside'].contains = items['Blue_Scroll']
room['overlook'].contains = items['White_Scroll']
room['narrow'].contains = items['Black_Scroll']



#
# Main
#
if __name__ == "__main__":
    print()

    done = False
    
    name = input("(Enter q to exit) Enter Name: ")
    print()
    print("choose between Paladin, Mage, or Archer")
    playerclass = input("(Enter q to exit) Enter Class: ")

    x = ["Paladin", "Mage", "Archer"]
    
    if playerclass != x[0] or x[1] or x[2] :
        print("You chose random")
        playerclass = random.choice(x)

    newPlayer = Player(name, room['outside'], playerclass)

    print()
    print(newPlayer.__str__())

    if name == "q":
        done = True

    def getItems():
        x = newPlayer.items
        if x == []:
            print(newPlayer.__str__())
            print()
            print("\"no items in inventory.\"")
        else:
            for item in x:
                print(item)
                

    def drop():
        x = newPlayer.items
        for r in x:
            if r.name == dif[1]:
                x.remove(r)
                print(f"{r.name} dropped")
            else:
                print("no item with such name in iventory")

    def search(current_room):
        if hasattr(current_room, 'contains'):
            x = getattr(current_room, 'contains')
            return x
        else:
            x = "\"Nothing of use was found.\""
            return x
     
    def pickup():
        if dif[2] == x.name:
            newPlayer.items.append(x)
            print(f"{dif[2]} added to inventory")
            for i in items:
                newPlayer.current_room.items.remove(i)
        else:
            print("no such item: "+ dir[2])

    def go_direction(dir, current_room):
        attribute = dir+'_to'
        if hasattr(current_room, attribute):
            # print(current_room.__str__())
            print(getattr(current_room, attribute))
            return getattr(current_room, attribute)
        else:
            print()
            print()
            print(newPlayer.__str__())
            print()
            print('\"You may not go this way!\"')
            
            return current_room



    while not done:
        
        

        print()
        print("Enter: \"n\", \"s\", \"e\", or \"w\"     move.")
        print("Enter: \"search\"                  search the room for items.")
        print("Enter: \"pick up (item)\"          pick up items.")
        print("Enter: \"drop (item)\"             drop items.")
        print("Enter: \"i\"                       view inventory.")
        print()

        dir = input("(Enter q to exit) What will you do: ")

        print()        
        print()
        print()

        dif = dir.rsplit(" ")
        

        if dir == "q":
            done = True

        if dir == "search":
            item = search(newPlayer.current_room)
            print( item )

        if dif[0] == "pick":
            pickup()
            
        if dir == "i":
            x = getItems()
            print()
        
        if dif[0] == "drop":
            drop()

        if dir in ("n", "s", "e", "w"):
            newPlayer.current_room = go_direction( dir, newPlayer.current_room)    

        
        

        continue  

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.