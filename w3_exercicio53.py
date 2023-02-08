"""
53. Write a Python program to access environment variables.
"""

import os

def show_environment_variables():
    """
    Prints environment variables
    """
    for i in os.environ:
        print(i)
        print(os.environ[i])

show_environment_variables()