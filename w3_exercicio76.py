"""
76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
"""

import sys

def command_line_arguments():
    print('Script Name: ', sys.argv[0])
    print('Number of arguments: ', len(sys.argv))
    print('Argument List: ', sys.argv)

command_line_arguments()