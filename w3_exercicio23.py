"""
23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
Return n copies of the whole string if the length is less than 2.
"""

def multiply_string(string, n):
    """
    Returns the first 2 characters of a string multiplied by "n" if len(string) >= 2, otherwise it returns the whole string * n

    The function receives a string and a number from the user and then if the string has less than 2 characters,
    it multiplies the whole string by the input number.If the string has 2 or more characters however, then it multiplies
    the first 2 characters of the string by the input number instead.

    Args:
    string = The string input by the user
    n = The number input by the user

    Returns:
    string * n if len(string) < 2
    string[:2] if len(string) >= 2
    """
    n = int(abs(n))
    if len(string) < 2:
        return string * n
    if len(string) >= 2:
        return string[:2] * n

print(multiply_string('sample', 13))