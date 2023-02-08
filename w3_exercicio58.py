"""
58. Write a Python program to sum the first n positive integers.
"""

def sum_positive_ints(n):
    """
    Returns the sum of the first n positive integers

    Args:
    n = the number of integers you'd like the sum of
    Returns:
    The total sum of the equation.
    """
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print(sum_positive_ints(30))