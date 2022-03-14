def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

upper_limit = 30

if upper_limit <= 0:
    pass
else:
    print('Fibonacci Sequence:')
    for x in range(upper_limit):
        print(fibonacci_recursive(x))
