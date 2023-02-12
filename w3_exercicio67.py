"""
67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.
"""

def kilopascals_conversion(kilopascal):
    pounds_per_square_inch = kilopascal / 6.895
    millimeter_of_mercury = kilopascal * 7.501
    atmosphere_pressure = kilopascal / 101.3
    return pounds_per_square_inch, millimeter_of_mercury, atmosphere_pressure

print(kilopascals_conversion(100))