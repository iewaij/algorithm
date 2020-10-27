"""
Given a positive number, print out all Fibonacci numbers smaller or equal to that number. For example, given the number 11 the program should print out: 1 1 2 3 5 8. The next Fibonacci number would be 13 which is already larger than 11.
"""

fibonacci_dict = {1:0, 2:1, 3:1}

def fibonacci_saved(n: int) -> list:
    if n not in fibonacci_dict:
        fibonacci_dict[n] = fibonacci_saved(n-2) + fibonacci_saved(n-1)
    return fibonacci_dict[n]

def fibonacci_leq(n: int) -> list:
    i = 1
    while True:
        if fibonacci_saved(i) <= n:
            i += 1
        else:
            fibonacci_list = list(fibonacci_dict.values())
            return fibonacci_list[:-1]
