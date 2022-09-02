"""Rogan Helm 3/4/22

Euclid's Algorithm for calculating the GCD.
"""


def main():
    if GCD(285, 255) == 15 and \
            GCD(110, 42) == 2 and \
            GCD(1540, 385) == 385 and \
            GCD(15, 7) == 1:

        print("Your code is working correctly!")

    else:
        print("There may be a mistake somewhere in your GCD code")


def GCD(a, b):
    r = a % b
    if r != 0:
        return GCD(b, r)
    else:
        return b


if __name__ == "__main__":
    main()
