"""Review questions

Author: Rogan Helm
Date: 04/22/2022
"""
import statistics

# Question 1
list_of_num = [0, 2, 7, 5, 6, 8, 12, 18, 3, 1]
for i in list_of_num:
    if i % 6 == 0:
        print(i)

# Question 2
new_list = []
for i in list_of_num:
    if i % 3 == 0 and i % 7 == 0:
        new_list.append(i)

# Question 3
print("Largest: ", max(list_of_num))
print("Smallest: ", min(list_of_num))
print("Average: ", statistics.mean(list_of_num))
print("Sum: ", sum(list_of_num))

# Question 4
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for i in range(1, 5):
    print("Week", i)
    for i in range(len(days_of_week)):
        print(" ", days_of_week[i] + ":")


# Question 5
def times_table(x: int, y: int) -> print:
    global i
    for i in range(1, y + 1):  # Prints the first vertical column of the table
        for e in range(1, x + 1):
            print(i * e, end=" ")
        print("\n")


times_table(10, 8)

# Question 6
# depth = int(input("Please enter the depth of the triangle: "))

# Question 7
list1 = ["cats", "1", "eggs", "bunny", "milk", "butter", "ashley"]
list2 = ["dogs", "2", "dogs", "milk", "bread", "matt", "dogs"]


def compare0(a, b):
    """Part a."""
    for i in a:
        if i in b:
            return i


def compare1(a, b):
    """Part b."""
    printed = []
    for i in a:
        if i in b:
            printed.append(i)
            for i in range(len(printed)):
                return printed[i]
        elif i in printed:
            for i in range(len(printed)):
                return printed[i]


# def compare2(a, b):
#     """Part c."""
#     printed = []
#     for i in a:
#         if i in b:
#             printed.append(i)
#             return i


def compare3(a, b):
    """Part d."""
    pass


# print(compare0(list1, list2))
print(compare1(list1, list2))
# print(compare2(list1, list2))
# print(compare3(list1, list2))
