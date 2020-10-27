def fibonaccisequence(a):
    if a <= 1:
        return a
    else:
        return (fibonaccisequence(a-1) + fibonaccisequence(a-2))
    
value_check = 50
start = 1
result = 0
while (value_check > result):
    result = fibonaccisequence(start)
    if result < value_check:
        print(result)
        start = start + 1
