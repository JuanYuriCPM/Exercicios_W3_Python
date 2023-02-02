"""
26. Write a Python program to create a histogram from a given list of integers.
"""

def create_histogram(x):
    for i in x:
        print(('X' * i))

create_histogram([1, 3, 5, 7, 5, 3, 1])