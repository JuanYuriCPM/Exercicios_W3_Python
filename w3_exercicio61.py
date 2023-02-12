"""
61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.
"""

def feet_to_inches(feet):
    return feet * 12

def feet_to_yards(feet):
    return feet / 3

def feet_to_miles(feet):
    return feet // 5280

print(feet_to_inches(20), feet_to_yards(20), feet_to_miles(20))