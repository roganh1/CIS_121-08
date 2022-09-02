import math


class SolarSystem:
    def __init__(self, aStar):
        self.star = aStar
        self.planets = []

    def show_star(self):
        print(self.star)

    def add_planet(self, aPlanet):
        self.planets.append(aPlanet)

    def show_planets(self):
        for aPlanet in self.planets:
            print(aPlanet)  # Alternatively print(aPlanet.get_name())


class Sun:
    def __init__(self, aName):
        self.name = aName

    def get_name(self):
        return self.name

    def set_name(self, newName):
        self.name = newName

    def __str__(self):
        return self.name


class Planet:
    def __init__(self, aName, aRadius, aMass, aDistance):
        self.name = aName
        self.radius = aRadius
        self.mass = aMass
        self.distance = aDistance

    def get_name(self):
        return self.name

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_dist(self):
        return self.distance

    def get_volume(self):
        return 4 / 3 * math.pi * self.radius ** 3

    def set_name(self, newName):
        self.name = newName

    def __leq__(self, aPlanet):
        if self.radius < aPlanet:
            return True
        else:
            return False

    def __str__(self):
        return self.name


class Star:
    def __init__(self, aName):
        self.name = aName

    def __str__(self):
        return self.name
