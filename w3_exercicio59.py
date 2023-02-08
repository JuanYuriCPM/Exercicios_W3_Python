"""
59. Write a Python program to convert height (in feet and inches) to centimeters
"""

def feet_and_inches_to_centimeters(n1, n2):
    """
    Converts feet and inches to centimeters

    Args:
    n1: value of feet
    n2: value of inches
    Returns:
    The converted values to centimeters.
    """
    return ((12*n1) + n2) * 2.54

print(feet_and_inches_to_centimeters(2, 20))