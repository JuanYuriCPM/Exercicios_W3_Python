"""
6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
"""


numbers = input('Enter the numbers you would like to add, separated by commas: ')
numbers_list = list(numbers.split(sep=', ' ))
numbers_tuple = tuple(numbers.split(sep=', '))
print(numbers)
print(numbers_list)
print(numbers_tuple)