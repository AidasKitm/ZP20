# integer, string, long, double, float, boolean, []

# ----------------Data Types----------------
skaicius = 0
sakinys = "stringas"
flag = False
counter = 0

# ----------------Data Structures----------------
skaiciu_list = [6, 2, 1, 6, 2, 78, 3, 2, 1]
list = ["Galaxy S20", "Iphone 12", "XiomiMI10"]
tv_list = ["silelis", "samsungTV", "LGTV"]
unikalus_zodziai = set(list) # other way of creating set {list}
kategorijos = {"mobile_phones": list, "TV": tv_list}

# ----------------Printing----------------
print(list)
print(unikalus_zodziai)
# ----------------Logical if statements----------------
if len(list) == 3:
    print(len(list))

if flag == True:
    print("Flag is true")
else:
    print("Flag was not true")

if list == tv_list:
    print(list + " and " + tv_list + "are the same list")
elif len(tv_list) == len(list):
    print("both lists have same amount of elements")
else:
    print("none of the criteria fits")

# bad logical statement example
# if list == tv_list:
#     print(list + " and " + tv_list + "are the same list")
# if len(tv_list) == len(list):
#     print("both lists have same amount of elements")
# else:
#     print("none of the criteria fits")


# ----------------Loops----------------
for i, v in enumerate(list):
    print(i, v)

while flag == False:
    counter += 1
    if counter == 100:
        flag = True
    print(counter)


# ----------------Functions/Methods/Classes----------------
def funkcija(sarasas, sarasas2):
    print(sarasas, sarasas2)


class Testas:
    def metodas(self, sarasas):
        print(sarasas)


# ----------------Function call/Method call
# ----------------Function call----------------
funkcija(list, tv_list)

# ----------------Method call----------------
t = Testas()
t.metodas(list)

# ----------------Accessing data structures----------------
# ----------------Access list index----------------
pirmas_indeksas = list[1]

print(pirmas_indeksas)

# ----------------Access dictionary keys/values----------------
print(kategorijos.items())


# ----------------Bubble sort algorithm----------------

#  [6,4,2,1,6,2,7,3] -> Bubble sort -> [1,2,2,3,4,6,6,7]
#  Takes 1st number 6 compares to 2nd number 4 -> 6 > 4 -> saves into variable temp -> number 6 switch places with number 4 using temp -> goes to next index

def bubble_sort():
    bubble_sort_list = [6, 4, 2, 1, 6, 2, 7, 3]
    did_finish_sorting = False

    while did_finish_sorting == False:
        did_sort_happen = False
        for i in range(len(bubble_sort_list) - 1):
            if bubble_sort_list[i] > bubble_sort_list[i + 1]:
                temp = bubble_sort_list[i]
                bubble_sort_list[i] = bubble_sort_list[i + 1]
                bubble_sort_list[i + 1] = temp
                did_sort_happen = True

        if did_sort_happen == False:
            break

    print(bubble_sort_list)


bubble_sort()


def fibonacci(fibonacci_index):
    # 0,1,1,2,3,5,8,13,21,34

    fibonacci_sequence_list = [0,1]
    if fibonacci_index < 2:
        return print("Low fibonacci number it's either 0 or 1")

    for i in range(fibonacci_index - 2):
        second_from_last_number = fibonacci_sequence_list[-2]
        last_number = fibonacci_sequence_list[-1]
        new_fibonacci = second_from_last_number + last_number
        fibonacci_sequence_list.append(new_fibonacci)

    print(fibonacci_sequence_list)

fibonacci(5)

# carry
# 990000000 + 10000000 Carry: 2
# 010101010 + 01019990
# # 0 + 0 = 0 Carry: 0
# 1 + 9 = 10  Carry: 1
# 1 + 0 = 1 Carry: 1
# 0 + 0 = 0 Carry: 1
# 1 + 9 = 10 Carry: 2
# 9 + 1 = 10 Carry: 3
# 1 + 1 = 2 Carry: 3
# 0 + 0 = 0 Carry: 3
# 1 + 1 = 2 Carry: 3
# 0 + 0 = 0 Carry: 3
def carry_counter(number1, number2):
    counter = 0
    maximum_lenght = max(len(str(number1)), len(str(number2)))
    carry_amount = 0
    for i in reversed(range(maximum_lenght)):
        carry_amount = number1 % 10 + number2 % 10 + carry_amount
        if carry_amount >= 10:
            carry_amount = 1
        else:
            carry_amount = 0
        counter += carry_amount
        number1 = number1 / 10
        number2 = number2 / 10

    print(f"Carry amount: {counter}")


carry_counter(990000000, 10000000)

