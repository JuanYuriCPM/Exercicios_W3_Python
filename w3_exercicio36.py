"""
36. Write a Python program to add two objects if both objects are integers
"""

def add_if_int(n1, n2):
    """
    Adds two objects if both are integers, otherwise it returns an error message

    Args:
    n1 = First object input by the user
    n2 = Second object input by the user

    Returns:
    n1 + n2 if both objects are int, an error message if they're not.
    """
    if type(n1) == int and type(n2) == int:
        return n1 + n2
    else:
        return 'At least one of the objects is not an int'

print(add_if_int(2, 5))