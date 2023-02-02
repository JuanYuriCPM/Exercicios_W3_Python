"""
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""

def expression(n):
    """
    Returns the sum of n + nn + nnn

    The function takes the number input by the user
    then creates 3 different variables with different combinations
    of 'n', and then converts then to int in order to solve
    the expression "n + nn + nnn"

    Args:
    n = the number used for the expression
    Returns:
    The result of the expression "n + nn + nnn
    """

    n1 = int(f'{n}')
    n2 = int(f'{n}{n}')
    n3 = int(f'{n}{n}{n}')
    return n1 + n2 + n3

print(expression(5))
