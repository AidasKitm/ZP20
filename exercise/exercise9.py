# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.
from random import randint

random_number = randint(1, 9)
count = 0
game_goes_on = True


def game_logic(random, user_input):
    if str(user_number) == "exit":
        return
    if random == int(user_input):
        print(f"You guessed the number correctly random was {random} and you guessed {user_input}")
        print(f"you took {count} times to guess correct number")
    elif random > int(user_input):
        print(f"random number is higher than your input {user_input}")
    elif random < int(user_input):
        print(f"random number is lower than your input {user_input}")


while game_goes_on:
    user_number = input("Guess the number or exit the game: ")
    count += 1
    game_logic(random_number, user_number)

    if user_number == random_number:
        random_number = randint(1, 9)
        count = 0
    if user_number == "exit":
        break
