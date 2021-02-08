# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock
import random

repeat_game = True


def rock_paper_scrissors(user_input, computer):
    if (user_input == "rock" and computer == "scissors") or (user_input == "paper" and computer == "rock") or (
            user_input == "scissors" and computer == "paper"):
        print("you won")
    elif (user_input == "rock" and computer == "rock") or (user_input == "paper" and computer == "paper") or (
            user_input == "scissors" and computer == "scissors"):
        print("It's a tie")
    else:
        print("You lose!")


while repeat_game == True:
    user_input = input("Pick rock,paper,scissors: ")
    computer = random.choice(["rock", "paper", "scissors"])
    rock_paper_scrissors(user_input, computer)
    second_user_input = input("Do you want to play again? Write n/y")
    if second_user_input == "n":
        repeat_game = False
        print("thank you for playing the game!")
