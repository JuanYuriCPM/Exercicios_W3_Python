"""4. Write a Python program that calculates the area of a circle based on the radius entered by the user. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504
Click me to see the sample solution"""

import math

radius = input('Please enter the radius: ')

print(f'Area = {(float(radius)**2) * math.pi}')