"""Rogan Helm 2/4/2022

This program will aEaten and print all the deficient numbers, perfect numbers, and
abundant numbers between 1 and some upper bound specified by the user.
"""
upperBound = int(input("Enter an upper bound for a check: "))
numOfDeficient = 0
numOfPerfect = 0
numOfAbundant = 0


def divisorSum(upper):
    """
    Sum of all a number's proper divisors
    """
    divSum = 0
    for n in range(1, upper + 1):
        if upper % n == 0:
            if n < upper:
                divSum += n
    return divSum


def propDivisors(upper):
    for n in range(1, upper):
        if upper % n == 0:
            return n


if divisorSum(propDivisors(upperBound)) > upperBound:
    for n in range(1, propDivisors(upperBound) + 1):
        numOfAbundant += 1

print(numOfAbundant)

# print("Between 1 and", upperBound, "there are")
# print(numOfDeficient, "deficient numbers")
# print(numOfPerfect, "perfect numbers")
# print(numOfAbundant, "abundant numbers")
