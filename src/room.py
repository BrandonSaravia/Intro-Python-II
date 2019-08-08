# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        # self.n_to = n_to
        # self.s_to = s_to
        # self.e_to = e_to
        # self.w_to = w_to

    def __str__(self):
        # for x in self:
        #     if self.x == null:
        #         self.x = "none"
        s = f"Location: {self.name}\nDescription: {self.description}"
        return s

#     def __repr__(self):
#         return f'Room({repr(self.name)}, {repr(self.description)})'

#     def getName(self):
#         return self.name

#     def setName(self, newValue):
#         self.name = newValue

#     def getDescription(self):
#         return self.description

#     def setDescription(self, newValue):
#         self.description = newValue

#     def getN_to(self):
#         return self.n_to

#     def setN_to(self, newValue):
#         self.n_to = newValue
    
#     def getS_to(self):
#         return self.s_to

#     def setS_to(self, newValue):
#         self.s_to = newValue
    
#     def getE_to(self):
#         return self.e_to

#     def setE_to(self, newValue):
#         self.e_to = newValue
    
#     def getW_to(self):
#         return self.w_to

#     def setW_to(self, newValue):
#         self.w_to = newValue

    
# w = Room("Main Room", "Lavashly decorated tall Room", "foyiegh", "dinning room", "ball room")
# print(w.getName())