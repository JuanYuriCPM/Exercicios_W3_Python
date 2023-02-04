"""
46. Write a Python program to retrieve the path and name of the file currently being executed.
"""

import os

print(f"The path of the file {os.path.basename(__file__)} is: {os.path.realpath(__file__)}")