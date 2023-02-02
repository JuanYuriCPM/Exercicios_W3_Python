"""
38. Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
"""

def calculate_formula(x, y):
    """
    Takes two values x and y, and calculates the result of (x + y) * (x + y)

    Args:
    x = First number
    y = Second number

    Returns: The result of (x + y) * (x + y)
    """
    return (x + y) * (x + y)

print(calculate_formula(4, 3))

