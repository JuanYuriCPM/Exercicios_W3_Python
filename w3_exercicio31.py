"""
31. Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
"""

def greatest_common_divisor(n1, n2):
    """
    Checks the greatest common divisor between 2 numbers and returns the highest one

    Calculates the greatest common divisor (gcd) between 2 numbers
    by setting the biggest number as the range, and then executing for loops
    in that range to check for numbers that have a remainder of 0 when dividing
    the 2 numbers input by the user.Then it adds all of then into a list and returns the
    last item in the list (the gcd)

    Args:

    n1 = the first number input by the user
    n2 = the second number input by the user
    """
    divisors = []
    if n2 > n1:
        for i in range(1, n1+1):
            if n1 % i == 0 and n2 % i == 0:
                divisors.append(i)
        return divisors[-1]
    elif n1 > n2:
        for i in range(1, n2+1):
            if n1 % i == 0 and n2 % i == 0:
                divisors.append(i)
        return divisors[-1]
    else:
        return n1

print(greatest_common_divisor(12,12))