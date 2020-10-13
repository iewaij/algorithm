"""
Given a sequence of numbers find any two numbers that add up to another given number. For example, given the sequence [3, 4, 1, 7, 9, 17] and the number 8, the solution is [1, 7], because these two add up to 8.
"""

def addup(a_sequence: list[int], a_number: int) -> tuple[int]:
    subset_list = []
    n = len(a_sequence)
    for i in range(n):
        e_i = a_sequence[i]
        a_sequence_removed = a_sequence[i+1:]
        for e_j in a_sequence_removed:
            subset_list.append((e_i,e_j))
    sum_dict = {}
    for t in subset_list:
        sum_dict[sum(t)] = t
    return sum_dict[a_number]
