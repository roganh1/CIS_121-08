from random import randint


class Die:
    def __init__(self, nSides):
        self.sides = nSides
        self.faceUpValue = 1

    def roll(self):
        self.faceUpValue = randint(1, self.sides)

    def get_value(self):
        return self.faceUpValue

    def __str__(self):
        return self.faceUpValue

    def __add__(self, dice2):
        return self.get_value() + dice2.get_value()

    def __gt__(self, dice2):
        if self.get_value() > dice2.get_value():
            return self.get_value()
        else:
            return dice2.get_value()


class Player:
    def __init__(self, aName):
        self.name = aName
        self.d1 = Die(6)
        self.d2 = Die(10)

    def roll_dice(self):
        self.d1.roll()
        self.d2.roll()

    def get_dice_value(self):
        return self.d1.get_value() + self.d2.get_value()

    def __str__(self):
        return self.name


class HighTwoGame:
    def __init__(self, name1, name2):
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def play_one_game(self):
        self.player1.roll_dice
        self.player2.roll_dice
        print(self.player1, "rolled", self.player1.get_dice_value())
        print(self.player2, "rolled", self.player2.get_dice_value())

    # def playManyGames(self, numGames):
    #     self.games2play = numGames
    #     HighTwoGame.play_one_game()

    def __str__(self):
        return self.player1, self.player2
