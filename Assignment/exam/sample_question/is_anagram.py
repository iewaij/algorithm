"""
Given two strings, determine if one is an anagram of the other. For example, the two strings “anagram” and “margana” are anagrams of each other.
"""

def is_anagram(string_1: str, string_2: str) -> bool:
    n = len(string_1)
    if len(string_2) != n:
        return False
    for i in range(n):
        if string_1[i] != string_2[-i-1]:
            return False
    return True
            
