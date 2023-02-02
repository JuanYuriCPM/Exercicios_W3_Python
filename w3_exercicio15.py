"""
15. Write a Python program to get the volume of a sphere with radius six.

V = 4/3 πr³
"""
import math

def sphere_volume(r):
    return (4/3)*(math.pi*(r**3))

print(sphere_volume(6))

