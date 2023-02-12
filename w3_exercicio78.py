"""
78. Write a Python program to find the available built-in modules.
"""

def get_info(module):
    return help(module)

print(get_info('math'))