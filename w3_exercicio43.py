"""
43. Write a Python program to get OS name, platform and release information.
"""

import os
import platform

def show_system_info():
    """
    Prints the name of the OS, the platform and the version of the platform
    """
    print(os.name)
    print(platform.system())
    print(platform.release())

show_system_info()

