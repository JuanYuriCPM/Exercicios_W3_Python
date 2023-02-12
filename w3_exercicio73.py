"""
73. Write a Python program to calculate the midpoints of a line.
"""

# The formula for midpoint = (x1 + x2)/2, (y1 + y2)/2.

def midpoints_of_line(x1, x2, y1, y2):
    return ((x1 + x2)/2), ((y1 + y2) /2)

print(midpoints_of_line(1, 2, 4, 5))