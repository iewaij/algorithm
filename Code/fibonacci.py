def fibonacci(n):
    if n == 1:
        return 0
    if n <= 3:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

# 0, 1, 1, 2, 3, 5, 8
print(fibonacci(5))

fibonacci_dict = {1:0, 2:1, 3:1}

def fibonacci_saved(
    n):
    if n not in fibonacci_dict:
        fibonacci_dict[n] = fibonacci_saved(n-2) + fibonacci_saved(n-1)
    return fibonacci_dict[n]

# 0, 1, 1, 2, 3, 5, 8
print(fibonacci_saved(50))

class Fibonacci:

    def __init__(self):
        self.dict = {1:0, 2:1, 3:1}

    def get(self, n):
        if n not in self.dict:
            self.dict[n] = self.get(n-2) + self.get(n-1)
        return self.dict[n]

fibonacci_object = Fibonacci()

print(fibonacci_object.get(50))
print(fibonacci_object.dict)
