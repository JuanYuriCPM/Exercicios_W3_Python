"""
30. Write a Python program that will accept the base and height of a triangle and compute its area.
"""

base = int(input('Enter the value for the base: '))
height = int(input('Enter the value for the height: '))

def triangle_area(b, h):
    """
    Calculates the area of a triangle of base "b" and height "h"

    Args:
    b = the base of the triangle
    h = the height of the triangle

    Returns:
    The area of the triangle (formula: (b*h)/2)
    """

    return (b*h)/2

print("The area of the triangle is: ", triangle_area(base, height))