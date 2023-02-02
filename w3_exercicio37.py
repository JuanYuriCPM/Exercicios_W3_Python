"""
37. Write a Python program that displays your name, age, and address on three different lines.
"""

def display_data(name, age, adress):
    """
    Takes all args and prints them in 3 separate lines

    Args:
    name = name input by the user
    age = age input by the user
    adress = adress input by the user
    """
    print(name)
    print(age)
    print(adress)


name = input('Enter your name: ')
age = input('Enter your age: ')
adress = input('Enter your adress: ')

display_data(name, age, adress)