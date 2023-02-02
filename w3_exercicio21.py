"""
21. Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
"""

def odds_or_even(n):
    """
    Checks wether a number is Odd or Even

    The function receives a number "n" input
    by the user and then returns a message
    that says "n" is even if "n" % 2 == 0, or it
    returns a message that says "n" is odd if
    "n" % 2 != 0.

    Args:
    n = The number input by the user

    Returns:
    A message saying wether the number input by the user is 
    Odd or Even.
    """


    if n % 2 == 0:
        return f'{n} is Even'
    else:
        return f'{n} is Odd'


n = input("Enter the number you'd like to evaluate: ")

print(odds_or_even(int(n)))