# Input
years = float(input("Enter your age: "))

# Calculate dog years
dogYrs = years * 7

# Calculate cat years
catYrs = years / 9

# Horse years
hrseAge = 3 * (((years ** 2 - 47) / 7) + 12)

# Isolate the decimal from the whole number to calculate the months and days
dMonths = (dogYrs - int(dogYrs)) * 12
dDays = (dMonths - int(dMonths)) * 30

cMonths = (catYrs - int(catYrs)) * 12
cDays = (cMonths - int(cMonths)) * 30

hMonths = (hrseAge - int(hrseAge)) * 12
hDays = (hMonths - int(hMonths)) * 30

# Output
print("Your age in dog years is ", int(dogYrs), " years, ", int(dMonths), " months, and ", int(dDays), " days.")
print("Your age in cat years is ", int(catYrs), " years, ", int(cMonths), " months, and ", int(cDays), " days.")
print("Your age in horse years is ", int(hrseAge), " years, ", int(dMonths), " months, and ", int(hDays), " days.")
