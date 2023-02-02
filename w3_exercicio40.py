"""
40. Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
"""

import math

def calculate_distance(x1, x2, y1, y2):
    """
    Calculates the distance between two points A and B given the coordinates (x1, y1) and (x2, y2)

    Args:
    x1 = coordinate X of point A
    x2 = coordinate X of point B
    y1 = coordinate Y of point A
    y2 = coordinate Y of point B

    Returns:
    The result of the square root of (y1 - x1)**2 + (y2 - x2)**2
    """
    return math.sqrt(((y1 - x1)**2) + ((y2 - x2)**2))

print(calculate_distance(4, 0, 6, 6))