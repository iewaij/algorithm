"""
Implement a Binary Search Tree and measure time complexity of get.

requirements: 
    faker
    numpy
    pandas
    seaborn
authors: 
    Akshat Bharti
    Vivian Jung-Loddenkemper
    Nasim Moeindarbari
    Jiawei Li
    Prashant Singh
date: 27/9/2020
"""

from IPython.display import set_matplotlib_formats
import time
from faker import Faker
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="white")
set_matplotlib_formats('retina')


class Node:
    def __init__(self, key, data):
        self.left = None
        self.right = None
        self.key = key
        self.data = data

    def get(self, key):
        if key == self.key:
            return self.data
        elif self.left is not None and key < self.key:
            return self.left.get(key)
        elif self.right is not None and key > self.key:
            return self.right.get(key)
        else:
            return None

    def insert(self, key, data):
        if key == self.key:
            self.data = data
        elif key < self.key:
            if self.left is None:
                self.left = Node(key, data)
            else:
                self.left.insert(key, data)
        else:
            if self.right is None:
                self.right = Node(key, data)
            else:
                self.right.insert(key, data)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def add_nodes(a_root, left_list, right_list):
    n_l = len(left_list)
    n_r = len(right_list)
    if n_l == 1 or n_r == 1:
        for i in left_list+right_list:
            a_root.insert(i[0], i[1])
    else:
        n_l_m = n_l // 2
        n_r_m = n_r // 2
        a_root.insert(left_list[n_l_m][0], left_list[n_l_m][1])
        a_root.insert(right_list[n_r_m][0], right_list[n_r_m][1])
        add_nodes(a_root, left_list[:n_l_m], left_list[n_l_m+1:])
        add_nodes(a_root, right_list[:n_r_m], right_list[n_r_m+1:])


def create_tree(n):
    fake = Faker(["en_US", "en_GB", "fr_FR", "it_IT", "de_DE"])
    name_list = [fake.first_name() + " " + fake.last_name() for i in range(n)]
    sorted_list = list(zip(range(1, n+1), name_list))
    n_m = n // 2
    tree = Node(sorted_list[n_m][0], sorted_list[n_m][1])
    add_nodes(tree, sorted_list[:n_m], sorted_list[n_m+1:])
    return tree


def record_complexity(end, step):
    size_array = np.arange(0, end+step, step)
    time_array = np.array([0.])
    for n in size_array[1:]:
        tree = create_tree(n)
        random_array = np.random.randint(0, n, 1000)
        start = time.time()
        for i in random_array:
            tree.get(i)
        end = time.time()
        time_array = np.append(time_array, end - start)
    complexity_data = pd.DataFrame({"size": size_array, "time": time_array})
    return complexity_data


complexity_data = record_complexity(100000, 2000)
fig = sns.relplot(x="size", y="time", kind="line", data=complexity_data)
