"""
A palindrome is sequence that reads same backwards as forwards. “Anna”, for example is a palindrome. The task is to determine if a given string is a palindrome.
"""

def is_palindrome(a_string: str) -> bool:
    a_string = a_string.lower()
    n = len(a_string)
    for i in range(n // 2):
        if a_string[i] != a_string[-i-1]:
            return False
    return True
