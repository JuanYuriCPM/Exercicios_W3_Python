"""
35. Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5
"""

def check_values(n1, n2):
    """
    Returns True if the two given integer values are equal or their sum or difference is 5

    Args:
    n1 = First number input by the user
    n2 = Second number input by the user
    
    Returns:
    True if n1 == n2 or n1 + n2 == 5 or abs(n1 - n2) == 5
    False if none of above conditions are met
    """
    if n1 == n2 or n1 + n2 == 5 or abs(n1 - n2) == 5:
        return True
    else:
        return False

print(check_values(5, 11))