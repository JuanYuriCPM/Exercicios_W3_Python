"""
68. Write a Python program to calculate sum of digits of a number.
"""

def sum_of_digits(number):
    sum = 0
    numberlist = list(str(number))
    for i in numberlist:
        sum += int(i)
    return sum

print(sum_of_digits(3764))