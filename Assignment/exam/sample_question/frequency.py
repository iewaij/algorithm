"""
Given a sequence of elements (that support equality function), calculate the frequency of each distinct element.
"""

from collections import defaultdict

def frequency(a_sequence: list[str]) -> defaultdict:
    frequency_dict = defaultdict(int)
    for e in a_sequence:
        frequency_dict[e] += 1
    return frequency_dict

if e not in frequency.keys():
    do_something
else:
    frequency_dict[e] += 1
