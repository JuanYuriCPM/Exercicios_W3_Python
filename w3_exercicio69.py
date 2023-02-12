"""
69. Write a Python program to sort three integers without using conditional statements and loops.
"""

def sort_ints(int1, int2, int3):
    intlist = [int1, int2, int3]
    return sorted(intlist)

print(sort_ints(5, 17, 4))