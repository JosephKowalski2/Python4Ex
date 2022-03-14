from random import randrange


def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)


number_range = randrange(0, 995)


if number_range == 0:
    print('The factorial of 0 is 1')
else:
    print(f'The factorial of {number_range} is {factorial(number_range)}')

