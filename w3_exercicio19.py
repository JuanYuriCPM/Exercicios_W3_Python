"""
19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. 
Return the string unchanged if the given string already begins with "Is".
"""

def add_is(string):
    if string[0:2] == 'Is':
        return string
    else:
        string = f'Is {string}'
        return string

print(add_is('I'))