"""
27. Write a Python program that concatenates all elements in a list into a string and returns it.
"""

def concatenate_list(list):
    string = ''
    for i in list:
        string += str(i)
    return string

print(concatenate_list(['a', 'b', 'c', ['a', 'b', 2]]))