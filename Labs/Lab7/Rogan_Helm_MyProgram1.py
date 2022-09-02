"""File: Rogan_Helm_MyProgram1.py 2/25/22

Calculates the mean, median, and mode of apples eaten during a 50-day period.
"""
import Rogan_Helm_Stats1

data = open("50DayFruitData.txt", "r")
output = open("Rogan_Helm_Output.txt", "w")
aEaten = []

for fruit in data:
    data = fruit.split()
    if data[1] == "apple":
        aEaten.append(int(data[2]))

output.write("The mean number of apples eaten is " + str(Rogan_Helm_Stats1.Mean(aEaten)) + "\n")
output.write("The median number of apples eaten is " + str(Rogan_Helm_Stats1.Median(aEaten)) + "\n")
output.write("The mode number of apples is (are) " + str(Rogan_Helm_Stats1.Mode(aEaten)))
output.close()
