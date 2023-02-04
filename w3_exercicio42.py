"""
42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
"""
import struct

def check_bit_mode(x):
    """
    Checks if Python Shell is executing on 32bit or 64bit mode

    Args:
    x = string input
    Returns:
    True 32 if system is 32 bit, 64 if system is 64 bit
    """
    return struct.calcsize(x) * 8

print(check_bit_mode("P"))
