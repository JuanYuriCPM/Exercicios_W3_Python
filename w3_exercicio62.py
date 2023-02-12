"""
62. Write a Python program to convert all units of time into seconds
"""

# Choosing not to add time units above months as the number would be too large to calculate and would probably brick my crappy ass notebook.

from math import exp

def convert_months(n):
    return n * 2.628*exp(6)

def convert_weeks(n):
    return n * 604800

def convert_days(n):
    return n * 86400

def convert_hours(n):
    return n * 3600

def convert_minutes(n):
    return n * 60

def convert_milliseconds(n):
    return n * 0.001

def convert_microsecond(n):
    return n * exp(-6)

def convert_nanosecond(n):
    return n * exp(-9)

print(convert_days(5), convert_milliseconds(10000), convert_months(2))