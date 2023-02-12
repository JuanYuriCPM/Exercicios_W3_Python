"""
66. Write a Python program to calculate the body mass index.
"""

def body_mass_index_calculator(weight, height):
# Weight in Kg, Height in meters
    return weight / (height ** 2)



print(body_mass_index_calculator(97, 1.80))