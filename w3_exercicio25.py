"""
25. Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""
group_of_values = [1, 5, 8, 3]

def check_value(n):
    """
    Checks wether or not "n" is in "group_of_values"

    Args:
    n = number input by the user
    group_of_values = the group of values analyzed

    Returns:
    True if n in group_of_values, False if not.
    """


    return n in group_of_values

print(check_value(-1))