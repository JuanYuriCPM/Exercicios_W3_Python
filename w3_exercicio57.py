"""
57. Write a Python program to get the execution time of a Python method.
"""

import time
def total_sum(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

print(total_sum(100000))