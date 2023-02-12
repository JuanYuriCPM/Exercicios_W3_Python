"""
65. Write a Python program that converts seconds into days, hours, minutes, and seconds.
"""
def seconds_conversion(seconds):
    days = seconds / 86400
    hours = seconds / 3600
    minutes = seconds / 60
    return f'Conversion {seconds} seconds to:\n\nDays: {days}\nHours: {hours}\nMinutes: {minutes}\nSeconds:{seconds}'

print(f' {seconds_conversion(60)}')