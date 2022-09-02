from math import comb


class Binomial:
    """Binomial class."""

    def __init__(self, x: int = "x", y: int = "y", n: None = "n"):
        """Use form (x+y)^n"""
        self.x = x
        self.y = y
        self.n = n

    def comb(self, n, k):
        return self.factorial(n) / (self.factorial(k) * self.factorial(n - k))

    def evaluate(self):
        """Evaluates the binomial."""
        if self.n is not None:
            return (self.x + self.y) ** self.n
        else:
            return self.x + self.y

    def expand(self):
        """Expands the Binomial."""
        coefficients = list()
        for k in range(0, self.n + 1):
            coefficients.append(self.comb(self.n, k))

    def factorial(self, n):
        if n == 1:
            return n
        elif n < 1:
            return "Factorial error"
        else:
            return self.factorial(n-1)

    def __str__(self):
        """Returns str representation of Binomial."""
        if self.n is not None:
            return f"({self.x}+{self.y})^{self.n}"

        elif self.x == "x":
            return f"(x+{self.y})"

        elif self.x == "x" and self.n is not None:
            return f"(x+{self.y})^{self.n}"

        elif self.y == "y":
            return f"({self.x}+y)"

        elif self.y == "y" and self.n is not None:
            return f"({self.x}+y)^{self.n}"


print(Binomial().comb(5, 6))
print(comb(5, 6))
binomial_0 = Binomial()
print(binomial_0)

binomial_1 = Binomial(4, 2, 5)
print(binomial_1)
print(binomial_1.evaluate())
print(binomial_1.expand())

# binomial_2 = Binomial('x', 2, 5)
# print(binomial_2)
# print(binomial_2.expand())
