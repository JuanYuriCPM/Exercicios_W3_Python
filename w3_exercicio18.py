"""
18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
"""

def sum_of_three(n1, n2, n3):
    """
    Returns the sum of three numbers and multiplies it by 3 if they're all equal

    Args:
    n1 = First Number
    n2 = Second Number
    n3 = Third Number

    Returns:
    3*(n1 + n2 + n3) if n1 == n2 == n3
    n1 + n2 + n3 if any is different
    """
    if n1 == n2 == n3:
        return 3*(n1 + n2 + n3)
    else:
        return n1 + n2 + n3

print(sum_of_three(3,3,3))