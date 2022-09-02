"""File: classes_rogan_helm.py

Author: Rogan Helm
Date: 4/2/22
This file contains the classes for the lab 11 project.
"""
from math import pi


class GeometricObject:
    """Base class for all objects."""
    def __str__(self):
        return None
    # TODO: Finish GeometricObject class


# class ThreeDimensionalObject:
#     def __init__(self):
#         self.volume = 0
#         self.surface_area = 0
#
#     def get_volume(self):
#         return self.volume
#
#     def get_surface_area(self):
#         return self.surface_area


class TwoDimensionalObject:
    """Base class for all two-dimensional objects. This class is meant to be subclassed."""
    def __init__(self, side_length, side_length2):
        super().__init__()
        self.sl = side_length
        self.sl2 = side_length2

    def get_area(self):
        """Gets area of a two-dimensional object."""
        return self.sl * self.sl2

    def get_perimeter(self):
        """Gets perimeter of a two-dimensional object."""
        return (2 * self.sl) + (2 * self.sl2)


class Rectangle(TwoDimensionalObject):
    """Subclasses the TwoDimensionalObject class."""
    def __init__(self):
        super().__init__()


class Square(Rectangle):
    """Subclasses the Rectangle class."""
    def __init__(self, side_length):
        """Constructor for the Square Class.

        Parameters
        ----------
        side_length
        """
        super().__init__()  # Inheritance used here


class Circle(TwoDimensionalObject):
    """Has methods to calculate the area and perimeter of a circle. Subclasses the TwoDimensionalObjectClass."""
    def __init__(self, radius):
        """Constructor for the Circle class. Creates the radius instance variable.

        Parameters
        ----------
        radius
        """
        super().__init__()  # Inheritance used here
        self.radius = radius
        # TODO: Double check Circle class and methods.

    def _calc_area(self) -> float:
        """Calculates the area of a circle."""
        return pi * self.radius ** 2

    def _calc_perimeter(self) -> float:
        """Calculates the perimeter of a circle."""
        return 2 * pi * self.radius

    def get_area(self) -> float:  # Polymorphism used here
        """Gets the area of a circle. Overrides the _get_area method in the super class."""
        return self._calc_area()

    def get_perimeter(self) -> float:  # Polymorphism used here
        """Gets the perimeter of a circle. Overrides the _get_perimeter method in the super class."""
        return self._calc_perimeter()


class Annulus(Circle):
    def __init__(self, radius, outer_radius):
        super().__init__(radius)  # Inheritance used here
        self.outer_radius = outer_radius

    def get_area(self):  # Polymorphism used here
        return self.outer_radius.get_area() - self.radius.get_area()

    def get_perimeter(self) -> float:
        return self.outer_radius.get_perimeter()


class EquilateralTriangle(TwoDimensionalObject):
    def __init__(self, side_length):
        super().__init__(side_length)

    def get_area(self):
        return (self.sl * self.sl) / 2

    def get_perimeter(self):
        return self.sl * 3
