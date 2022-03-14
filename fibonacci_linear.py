def fibonacci(n):
    if n < 1:
        return n
    first_number, fibonacci_number = 0, 1
    for x in range(2, n + 1):
        first_number, fibonacci_number = fibonacci_number, first_number + fibonacci_number

    return fibonacci_number


print(fibonacci(6))
