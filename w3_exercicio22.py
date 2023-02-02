"""
22. Write a Python program to count the number 4 in a given list.
"""



def count_the_fours(list):
    total = 0
    for i in list:
        if i == 4:
            total += 1
    return total



print(count_the_fours([4, 5, 4, 3, 5, 4, 4, 5, 4]))