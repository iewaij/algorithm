"""
Given a sequence of numbers, determine the longest streak of consecutive numbers that are increasing. For example given the sequence [1, 2, 5, 3, 8, 9, 13, 24, 21], the longest sequence is [3, 8, 9, 13, 24].

Narrative: divide the sequence into smaller sequences which have only increasing numbers and compare the smaller sequence with the previous sequence, if the new sequence is longer then the previous sequence, keep the new sequence. When the division completes, return the small sequence which is also the longest.
"""

def increasing_section(a_sequence: list[int]) -> list[int]:
    n = len(a_sequence)
    section_list = []
    tmp_list = [a_sequence[0]]
    for i in range(1, n):
        e_p = a_sequence[i-1]
        e_i = a_sequence[i]
        if e_i > e_p:
            tmp_list.append(e_i)
        elif len(tmp_list) > len(section_list):
            section_list = tmp_list
            tmp_list = [e_i]
        elif i == n-1 and :
    if len(tmp_list) > len(section_list):
                section_list = tmp_list
    return section_list




