"""Rogan Helm 3/18/22

This implements the RoboFriend class.
"""


class RoboFriend:
    def __init__(self, aName, anAge):
        self.name = aName
        self.age = anAge

    def stateName(self):
        print("Hi! My name is", self.name)

    def stateAge(self):
        print("I'm", str(self.age), " years old.")
