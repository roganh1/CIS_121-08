def Mean(data):
    """Calculates the mean of the given values.

    :type data: list
    :param data: Numeric input
    :return: Mean of input
    """
    mean = sum(data) / len(data)
    return mean


def Median(data):
    """Calculates the median of the given values.

    :type data: list
    :param data: Numeric input
    :return: Median of input.
    """
    y = len(data)
    for x in data[0:]:
        if x == data[(y // 2)]:
            return x
        if x == data[(y % 2)]:
            return x
