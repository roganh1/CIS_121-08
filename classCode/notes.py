# <string> [<int>]
# # this repeats the <int>'s place in line
# name = "Rogan"
# name[0] = "R"
# name[1] = "o"
# name[4] = "n"
# name[-1] = "n"
# name[-2] = "a"
# ---------------
# fullName = "Rogan Helm"
# firstName = fullName[0:5] # 0 is inclusive and 5 is exclusive
# lastName = fullName[5:] # Colon without an index after it goes until the end of the string
# ---------------
# fullName = "Rogan Helm"
# first = ""
# last = ""
#
# numOfSpaces = 0
# for letter in fullName:
#     if letter == " ":
#         numOfSpaces += 1
#     elif numOfSpaces == 0:
#         first += 1
#     elif numOfSpaces >= 1:
#         last += letter
#
# print(first)
# print(last)
# ---------------
# """
# String slicing
# """
# fileList = ["myfile.txt", "myprogram.bin", "yourfile.txt"]
# for fileName in fileList:
#     if fileName[-4:] == ".txt":
#         print(fileName)
# for fileName in fileList:
#     if ".bin" in fileName:
#         print(fileName)
# ---------------
# def EncryptText(shift):
#     plainTxtMsg = input("Enter a message to be encrypted: ")
#     shift = 3
#     cipherTxtMsg = ""
#     for ch in plainTxtMsg.lower():
#         if ch == " ":
#             cipherTxtMsg += " "
#         else:
#             tempNumber = ord(ch)  # ord() gets the ASCII number
#             tempNumber -= 97
#             tempNumber += 3
#             tempNumber %= 26
#             tempNumber += 97
#             cipherTxtMsg += chr(tempNumber)
#     print(cipherTxtMsg)
#
#
# cipherTxtMsg = input("Enter a message to be decrypted: ")
# shift = 3
# plainTxtMsg = ""
# for ch in cipherTxtMsg.lower():
#     if ch == " ":
#         plainTxtMsg += " "
#     else:
#         tempNumber = ord(ch)  # ord() gets the ASCII number
#         tempNumber -= 97
#         tempNumber += 3
#         tempNumber %= 26
#         tempNumber += 97
#         plainTxtMsg += chr(tempNumber)
# print(plainTxtMsg)
#
# done = False
# while not done:
#     keepGoing = input("Would you like to encrypt another number? (Y/N): ")
#     if keepGoing.lower() == "n":
#         done = True
#     elif keepGoing.lower() == "y":
#         shift = int(input("Pick an integer shift: "))
#         EncryptText(shift)
#     else:
#         print("Invalid input")
# ---------------
# """
# 2/14/22
# Use files as inputs && create output files
# Unit 4.3
# """
# import random
#
# newFile = open("integers.txt", "r")  # w for write and r for read.
#  ^ assigns the contents of the integers.txt file to the newFile variable
#
# for count in range(500):
#     number = random.randint(1, 300)
#     newFile.write(str(number) + "\n")
#
# for line in newFile:
#     line = line.strip()  # removes \n
#     print(line)
# newFile.close()  # ALWAYS close file, or else the program won't proceed
#
# while True:            == (maybe?)   for line in newFile:
#     line = newFile.readline()            line = line.strip()  # removes \n
#                                          print(line)
#
# text = newFile.read()  # Entire aList is assigned to the text variable
# ---------------
# newFIle = open("SampleOutput.txt", 'w')
#
# next(newFile)
# for line in myFile:
#     newFile.write("The vaccination rate of is is 1.2f \n" % \
#                   (line.split(',')[0], int(line.split(','[2]) / int(line.split(',')[1]))))
# newFIle.close()
#
# ---------------
#
# countyNameLookup = input("Which county would you like to view statistics for? ")
#
# printed = False
# for line in myFile:
#     if countyNameLookup in line:
#         print("The vaccination rate of ")
# ---------------
# myList = []
# myList.append(3)
# myList.append("Dog")
# print(myList)
# Sentence = "This Sentence is six words long."
# words = Sentence.split()
# print(words)
# ---------------
# import statistics
#
#
# def Amount(aList):
#     count = len(aList)
#     return count
#
#
# def Summation(aList):
#     result = 0
#     y = len(aList)
#     while aList[0] <= aList[y]:
#         result += aList[0]
#         aList[0] += 1
#     return result
#
#
# def Mean(aList):
#     total = Summation(aList)
#     count = Amount(aList)
#     return total / count
#
#
# def main():
#     listOfNum = [3, 5, 1, 7, 12, 8, 9]
#     print("Hello")
#     print(statistics.mean(listOfNum))
#     print("Goodbye")
#
#
# ---------------
# def Fact(n):
#     num = 1
#     for i in range(1, n + 1):
#         num = num * i
#     return num
#
#
# def RecursiveFactorial(n):
#     if n == 1:
#         return 1
#     return n * RecursiveFactorial(n - 1)
# ---------------
# import math
# from functools import reduce


# def functionName(required1, required2, optional1=7, optional2="hi"):
#     print(required1)
#     print(required2)
#     print(optional1)
#     print(optional2)


# myList = [1, 3.2, "Hello", [1, 2]]
# funcs = [abs, math.sqrt]


# def AddOne(number):
#     return number + 1


# def TimesTwo(number):
#     return number * 2


# def MakeOdd(number):
#     return AddOne(TimesTwo(number))


# words = ['2', '23', '7', '8']
# print(map(int, words))  # map function applies the function in spot one (in this case int) to the list in spot two

# print(words)

# words = list(map(int, words))
# print(words)


# # We want the odd number from 1-10.

# def Odd(n):
#     return n % 2 == 1


# oddNumbers = list(filter(Odd, range(1, 11)))
# print(oddNumbers)


# def Add(x, y):
#     return x + y


# theSum = 0
# for i in range(0, 11):
#     theSum = Add(theSum, i)

# data = [1, 2, 3, 4, 5]
# print(reduce(Add, data))
# # We can use a lambda to create a function on the fly, a lambda is an anonymous function. (A function with no name)
# # Syntax:
# # lambda <[args]>: <expression>
# reduce(lambda x, y: x + y, data)  # Use this instead of the Add function made above.
# # A tuple is an immutable version of a list myList = ("M", "T", "W", "T", "F")
# # myList = list(myTuple)
# # myTuple = (tuple(myList))
# ---------------
# building classes
# class className:
#     def method1 ():
#         foo


#     def method2 ():
#         bar
# ---------------
# import Name ---- imports module Name and creates a reference to it in the current namespace. You then need to use
# the complete path to access a particular attributor method. ex Name.methodName()

# from Name import * ---- This imports Name, and creates a reference to add public objects defined by that module.
# use methodName() Name.methodName() will produce an error.
# ---------------
# private methods can only be used by the class they are from
# protected methods can only be accessed by the class they are from and any child classes
# observer patterns (not used in this class but research anyways)
