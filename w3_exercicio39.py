"""
39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
"""

def calculate_future_value(amount, interest, years):
    """
    Calculates the total amount owed based on the initial amount, interest and time passed (years)

    Args:
    amount = The initial amount owed
    interest = The interest by wich the initial amount should be increased every year
    years = The number of years that have passed
    """
    for i in range(1, years+1):
        amount += (amount * (interest/100))
    return amount

print(calculate_future_value(10000, 3.5, 7))