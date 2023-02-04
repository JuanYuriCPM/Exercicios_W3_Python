"""
49. Write a Python program to list all files in a directory. 
"""

from os import listdir

from os.path import isfile, join


def files_list(directory):
    """
    Prints every file in a specified directory, if the file exists in that directory.

    Args:
    directory = The directory being scanned

    Returns:
    Every file in the directory being scanned, if the file exists in that directory.
    """


    return [f for f in listdir(directory) if isfile(join(directory, f))]

print(files_list('Exercicios_W3_Python'))