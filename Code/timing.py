"""
Time calculation of insertion sort in Python.

filename: timing.py
author: Jiawei Li
date: 11/9/2020
version: 0.1
"""

import random
import time

def create_lists(n):
    number_list = list(range(0, n))
    reverse_list = list(range(n, 0, -1))
    random_list = random.sample(range(0, n), n)
    return [number_list, reverse_list, random_list]

def sort_a_list(a_list):
    for i in range(1, len(a_list)):
        while i > 0 and a_list[i] < a_list[i-1]:
            a_list[i-1], a_list[i] = a_list[i], a_list[i-1]
            i -= 1
    return a_list

def timing(n):
    number_lists = create_lists(n)
    number_names = ["ordered", "reverse", "random"]
    for (number_list, number_name) in zip(number_lists, number_names):
        start = time.time()
        for i in range(1000):
            sort_a_list(number_list)
        end = time.time()
        print("Timing of", n, number_name, "numbers", "is:", end - start)

# timing(1000)
# timing(2000)
# timing(4000)
# timing(8000)
# timing(16000)
# timing(32000)

[1, 2, 3, 4]
["a", "b", "c", "d"]
