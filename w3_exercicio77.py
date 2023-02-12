"""
77. Write a Python program to test whether the system is a big-endian platform or a little-endian platform.
"""

import sys

if sys.byteorder == 'big':
    print('Big-endian Platform')
else:
    print('Little-endian Platform')