"""
33. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
"""

def sum_of_three(n1, n2, n3):
    """
    Takes three numbers and calculates their sum.If 2 values are equal however, the sum is zero.

    Args:

    n1 = First number input by the user
    n2 = Second number input by the user
    n3 = Thrid number input by the user

    Returns:
    The sum of the three numbers, or 0 if two of them are equal.
    """

    if n1 == n2 or n1 == n3 or n2 == n3:
        return 0
    else:
        return n1 + n2 + n3

print(sum_of_three(4, 2, 3))