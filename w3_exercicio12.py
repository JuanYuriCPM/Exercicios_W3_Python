"""
12. Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
"""

import calendar

year = input("Enter the year: ")
month = input("Enter the month: ")

print(calendar.month(int(year), int(month)))