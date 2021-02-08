from random import randint

# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
#
# Extras:
#
#     Randomly generate two lists to test this
#     Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# random_list = []
# for n1 in a:
#     if n1 in b and n1 not in random_list:
#         random_list.append(n1)
#
# print(random_list)

list_comperhension = set([n1 for n1 in a if n1 in b])
print(list_comperhension)

