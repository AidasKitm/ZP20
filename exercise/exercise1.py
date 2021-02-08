# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
#
#     Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
#     (Hint: order of operations exists in Python)
#     Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
#

user_name_input = input("Write your name down: ")

user_age = int(input("Write your age down: "))

user_times_repeat = int(input("how many times do you want to repeat the last sentence: "))

expected_age_to_reach_100 = (2021 + 100 - user_age)

print(f"This year is 2021 in year {expected_age_to_reach_100} \n" * user_times_repeat)