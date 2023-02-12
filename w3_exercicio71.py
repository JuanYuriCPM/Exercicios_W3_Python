"""
71. Write a Python program to get a directory listing, sorted by creation date.
"""

import os
import time

def sort_dir_by_creation_dat(directory):
    sorted_list = sorted([(os.path.getctime(i), i) for i in os.listdir(directory)])
    for i in sorted_list:
        print(i[1])


sort_dir_by_creation_dat(r'C:\Users\juany\OneDrive\Desktop\curso_python')