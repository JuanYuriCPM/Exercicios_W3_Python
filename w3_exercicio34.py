"""
34. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
"""

def sum_of_two(n1, n2):
    """
    Returns the sum of two given numbers, or 20 if the sum is between 15 and 20.

    Args:
    n1 = First number input by the user
    n2 = Second number input by the user

    Returns:
    n1 + n2, or 20 if n1 + n2 is in range(16,20)
    """

    if n1 + n2 in range(16,20):
        return 20
    else:
        return n1 + n2

print(sum_of_two(10, 5))