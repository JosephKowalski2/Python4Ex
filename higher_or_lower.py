from random import randrange


def compare_user_number_and_random_number():
    number = 0
    random_number = randrange(10)
    while number != random_number:
        number = int(input("Please enter a number 1 to 10 \n"))
        if number > random_number:
            print("Your guess was too high")
            continue
        elif number < random_number:
            print("Your guess was too low")
            continue

    print("You guessed right!")
    print(f'You guessed {number}')
    print(f'The number was {random_number}')


compare_user_number_and_random_number()

