"""
Estimate the time complexity of merge sort for the best, reverse and worst cases.

filename: merge_timing.py
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
    return {"Best Case": number_list, "Reverse Case": reverse_list, "Worst Case": random_list}

def reduce(left_list, right_list):
    left_i = 0
    right_i = 0
    result_i = 0
    result_list = []
    while left_i < len(left_list) and right_i < len(right_list):
        if left_list[left_i] < right_list[right_i]:
            result_list.append(left_list[left_i])
            left_i += 1
        else:
            result_list.append(right_list[right_i])
            right_i += 1
        result_i += 1
    result_list.extend(left_list[left_i:])
    result_list.extend(right_list[right_i:])
    return result_list

def merge_sort(sort_list):
    if len(sort_list) <= 1:
        return sort_list
    else:
        n= len(sort_list)
        n_mid= n // 2
        left_list = sort_list[: n_mid]
        left_list = merge_sort(left_list)
        right_list = sort_list[n_mid: ]
        right_list = merge_sort(right_list)
        result_list= reduce(left_list, right_list)
        return result_list

def record_time():
    time_dataframe = pd.DataFrame(columns=["n", "Cases", "Time"])
    for n in range(100, 10100, 100):
        number_dict = create_lists(n)
        for item in number_dict.items():
            start = time.time()
            merge_sort(item[1])
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

# The shape of worst case in the plot suggests that the time complexity is linear and
# merge sort is a more efficient algorithm compared to insertion sort.
plot_time()
