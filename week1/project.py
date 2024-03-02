"""
Number Guessing Game
"""
import random


def generate_random_number():
    return random.randint(1, 100)


def get_user_guess():
    guess = int(input("Enter your guess: "))
    return guess


def play_game():
    random_number = generate_random_number()
    guess_attempt = 5

    while guess_attempt > 0:
        guess = get_user_guess()
        if guess == random_number:
            print("You win")
            break
        elif guess < random_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        guess_attempt = guess_attempt - 1

    if guess_attempt == 0:
        print("You loose")


play_game()

print("Thank you for playing.")
