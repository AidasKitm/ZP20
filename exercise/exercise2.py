# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#     If the number is a multiple of 4, print out a different message.
#     Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#     If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


user_input = int(input("Write a number:"))


if user_input % 4 == 0:
    print(f"{user_input} is divisible by 4")
elif user_input % 2 == 0:
    print(f"{user_input} is even number")
else:
    print(f"{user_input} is odd number")


user_num = int(input("Write a number"))
user_check = int(input("Write a check number"))

if user_num % user_check == 0:
    print(f"{user_num} evenly divided from {user_check}")
else:
    print("could not divide evenly")