from turtle import Turtle
from math import sqrt


def main():
    drawSnowflake(200, 200, 150, 2)


def drawSnowflake(width, height, size, level):
    """Draws a Koch snowflake with the given dimensions."""
    t = Turtle()
    dist = sqrt(width ** 2 + height ** 2)

    def drawFractalLine(dist, angle):
        t.forward(dist)
        t.setheading(-angle)
        t.forward(dist)
        t.setheading(angle)
        t.forward(dist)

    for count in range(level):
        while count == 0:
            drawFractalLine(200, 120)
            break


if __name__ == "__main__":
    main()
