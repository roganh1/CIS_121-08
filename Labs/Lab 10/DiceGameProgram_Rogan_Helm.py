"""Author: Rogan Helm

3/22/22
This program is a two player dice game called High Two. The player with the higher sum wins.
"""
from DiceGameClasses_Rogan_Helm import *

print("Game one:")
game1 = HighTwoGame("Matt", "Ashley")
game1.play_one_game()

print("")
print("Game two:")
game2 = HighTwoGame("Dexter", "Eugene")
game2.play_one_game()
