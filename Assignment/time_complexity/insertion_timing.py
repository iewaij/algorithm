"""
Estimate the time complexity of insertion sort for the best, average and worst cases.

filename: insertion_timing.py
author: Jiawei Li
date: 20/9/2020
"""

import time
import pandas as pd
from random import sample
import altair as alt

def create_lists(n):
    number_list = list(range(0, n))
    reverse_list = list(range(n, 0, -1))
    random_list = sample(range(0, n), n)
    return {"Best Case": number_list, "Worst Case": reverse_list, "Average Case": random_list}

def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        while i > 0 and a_list[i] < a_list[i-1]:
            a_list[i-1], a_list[i] = a_list[i], a_list[i-1]
            i -= 1
    return a_list

def record_time():
    time_dataframe = pd.DataFrame(columns=["n", "Cases", "Time"])
    for n in range(100, 10100, 100):
        number_dict = create_lists(n)
        for item in number_dict.items():
            start = time.time()
            insertion_sort(item[1])
            end = time.time()
            time_dataframe = time_dataframe.append({"n": n, "Cases": item[0], "Time": end - start}, ignore_index=True)
    return time_dataframe

def plot_time():
    time_dataframe = record_time()
    chart = alt.Chart(time_dataframe).mark_line().encode(
            x="n:Q",
            y="Time:Q",
            color="Cases:N")
    return chart

# The shape of worst case in the plot suggests that the time complexity is non-linear and quadratic.
plot_time()
