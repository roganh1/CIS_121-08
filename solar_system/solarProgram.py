"""
Rogan Helm

3/28/22
"""
from solar_system.SolarSystem import *

theSun = Star("The Sun")

ss = SolarSystem(theSun)
ss.show_star()

p = Planet("Earth", 50, 60, 30)
ss.add_planet(p)

p = Planet("Mars", 47, 50, 35)
ss.add_planet(p)

p.get_name()

p = Planet("Jupiter", 75, 100, 50)
ss.add_planet(p)

ss.show_planets()
