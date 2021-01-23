### LISTS - COMMA SEPERATED VALUES INSIDE SQUARE BRACES.

fruits = ["apples", "potatoes", "yams"]

print(fruits)
print("Variable fruits is of type -: ", type(fruits))

### ADD TO THE FRUITS LIST USING APPEND

fruit_to_add = "fish"

print()
fruits.append(fruit_to_add)
print("## AFTER APPENDING")
print(fruits)

print()
fruits.append([1,2,3,4])
print("## AFTER APPENDING")
print(fruits)

### REMOVE YAMS FROM LIST USING REMOVE METHODS

print()
print("## AFTER REMOVE")
fruits.remove("yams")
print(fruits)

### COUNT NUMBER OF ITEMS IN LIST USING .COUNT METHOD

print()
fruits.append("apples")
number_of_times_apples_occures_in_list = fruits.count("apples")
print("Apples occurs : ", number_of_times_apples_occures_in_list)


# INDEXING LISTS

# print(fruits[1])
# print()

# for i in range(4):
#     print(fruits[i], "- at position ", i)

# i = 0
# while i < 4:
#     print(fruits[i], "- at position ", i)
#     i += 1

# SLICING LIST

print()

data_list = ["ali", "benky", "sule", 2, 3, 12, 14, True, False, True, False]

# strings = data_list[0:3]
# numbers = data_list[3:7]
# booleans = data_list[7:12]
# jumping_steps = data_list[0:12:3]

# print("Strings List -->", strings)
# print("Numbers list -->", numbers)
# print("Booleans list -->", booleans)
# print("Jumping step list -->", jumping_steps)

even_numbers = []

for value in data_list:
    try:
        if value%2 == 0:
            print(value, "is an even number.")
            even_numbers.append(value)
            # print(value%2)
        else:
            print(value, "is an odd number.")
    except:
        print(value, "is not a number. Skipping..!!!")

print(even_numbers)