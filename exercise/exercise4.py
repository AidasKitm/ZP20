# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

divisor_list = []
user_input = int(input("Write a number:"))


def divisors(user_input):
    for number in range(1, user_input + 1):
        if user_input % number == 0:
            divisor_list.append(number)


divisors(user_input)

print(divisor_list)