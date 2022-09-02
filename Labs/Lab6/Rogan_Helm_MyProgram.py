import Rogan_Helm_Stats

data = open("500DayFruitData.txt", "r")
output = open("Rogan_Helm_Output.txt", "w")
aEaten = []

for fruit in data:
    data = fruit.split()
    if data[1] == "apple":
        aEaten.append(int(data[2]))

output.write("The mean number of apples eaten is " + str(Rogan_Helm_Stats.Mean(aEaten)) + "\n")
output.write("The median number of apples eaten is " + str(Rogan_Helm_Stats.Median(aEaten)))
output.close()
