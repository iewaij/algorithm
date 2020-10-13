"""
Given a sequence of numbers, determine if each element is larger than the previous element.
"""

def is_increasing(a_sequence: list[int]) -> bool:
    a_zip = zip(a_sequence[:-1], a_sequence[1:])
    for t in a_zip:
        if t[0] > t[1]:
            return False
    return True
