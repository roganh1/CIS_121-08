"""File: Rogan_Helm_Stats1.py 2/25/22

My own statistics library.
"""


def Mean(aList):
    """Calculates the mean of the given values.

    :type aList: list
    :param aList: Numeric input.
    :return: Mean of input, rounded to two decimal places.
    """
    mean = sum(aList) / len(aList)
    return round(mean, 2)


def Median(aList):
    """Calculates the median of the given values.

    :type aList: list
    :param aList: Numeric input
    :return: Median of input.
    """
    y = len(aList)
    for x in aList[0:]:
        if x == aList[(y // 2)]:
            return x
        if x == aList[(y % 2)]:
            return x


def Counter(aList):
    """Counts how many times an item in a list appears in the list.

    :type aList: list
    :rtype: dict
    :param aList:
    """
    theCount = {}

    for x in aList:
        if x in theCount:
            theCount[x] += 1
        if x not in theCount:
            theCount[x] = 1
    return theCount


def Mode(aList):
    """Calculates the mode of the given values.

    :type aList: list
    :param aList: Numeric input.
    :return: Mode of input.
    """
    theCount = Counter(aList)
    maximum = 0
    modes = []

    for x in theCount:
        count = theCount[x]
        if count > maximum:
            maximum = count
        if count == maximum:
            modes.append(x)
    return modes
