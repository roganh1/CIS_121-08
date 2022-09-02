"""
Rogan Helm
4/1/22

This code will test your created classes
"""

from classes_Rogan_Helm import *


def main():
    compare_get_sa_to_vol_ratio(1)
    compare_get_sa_to_vol_ratio(10)
    compare_get_sa_to_vol_ratio(25.6)


def compare_get_sa_to_vol_ratio(common_side_length):
    tetrahedron = Tetrahedron(common_side_length)
    print("The SA:V of a tetrahedron is " + str(tetrahedron.get_sa_to_vol_ratio()))

    cube = Cube(common_side_length)
    print("The SA:V of a cube is " + str(cube.get_sa_to_vol_ratio()))

    octahedron = Octahedron(common_side_length)
    print("The SA:V of a octahedron is " + str(octahedron.get_sa_to_vol_ratio()))

    icosahedron = Icosahedron(common_side_length)
    print("The SA:V of a icosahedron is " + str(icosahedron.get_sa_to_vol_ratio()))


if __name__ == "__main__":
    main()
