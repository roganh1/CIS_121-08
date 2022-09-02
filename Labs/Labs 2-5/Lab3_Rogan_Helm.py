"""Rogan Helm 1/28/22

Tax-debt calculator
"""
import sys

taxOwed = 0.0

earnedIncome = float(input("Enter the amount of income you earned in 2021: "))
if earnedIncome < 0:
    print("You made less than $0. Contact an accountant")
    sys.exit()

print("Are you married or single?")
maritalStatus = input("Type m for married and s for single: ")

# Ensures you have a valid marital status
while maritalStatus != "m" and maritalStatus != "s":
    print("you entered an invalid marital status")
    maritalStatus = input("Type m for married and s for single: ")

# Your code goes here
if maritalStatus == "s":
    if earnedIncome <= 9950:
        taxOwed += .1 * earnedIncome
    else:
        if earnedIncome <= 40525:
            taxOwed += .1 * 9950
            taxOwed += .12 * (earnedIncome - 9950)
        else:
            if earnedIncome <= 86375:
                taxOwed += .1 * 9950
                taxOwed += .12 * (earnedIncome - 9950)
                taxOwed += .22 * (earnedIncome - 40525)
            else:
                print("You made too much money for this calculator. Hurray!")
if maritalStatus == "m":
    if earnedIncome <= 19900:
        taxOwed += .1 * earnedIncome
    else:
        if earnedIncome <= 81050:
            taxOwed += .1 * 19900
            taxOwed += .12 * (earnedIncome - 19900)
        else:
            if earnedIncome <= 172750:
                taxOwed += .1 * 19900
                taxOwed += .12 * (earnedIncome - 19900)
                taxOwed += .22 * (earnedIncome - 81050)
            else:
                print("You made too much money for this calculator. Hurray!")
print("This year you owe ", taxOwed, " in taxes")
