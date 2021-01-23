# word = "conquistadore"
# target = "q"
# # target in word
# for i in word:

#     if i == target:
#         print(f"Found letter {target}.")
#         break
#     else:
#         print("Not found")

# else:
#     print("All values were tested and target was not found.")


# WHILE LOOPS
import time

# while True: # INFINITE LOOP
#     print("Running")
#     print("Standing")
#     time.sleep(1)

# condition = True

# while condition: # INFINITE LOOP
#     print("Running")
#     print("Standing")
#     time.sleep(1)

# start = 5
# end = 0
# interval = -1

# while True:
#     start += interval
#     print(start)

#     if start == end:
#         break


# start = 5
# end = 0
# interval = -1

# while True:
#     start += interval
#     print(start)

#     if start == end:
#         break


# target = "Mr"
# staffs = ["Mr ali", "Master tunde", "Mrs salami", "Dr saheed", "Mr layi"]

# for staff in staffs:
#     if target in staff and not staff.startswith("Mrs"):
#         print(staff)

# else:
#     print(f"Sorry no staff with {target} salutation.")

# target = "Mr"
# staffs = ["Mr ali", "Master tunde", "Mrs salami", "Dr saheed", "Mr layi"]

# for staff in staffs:
#     print(staff.split(" "))
#     if staff.split(" ")[0] == target:

#         print(staff)

# else:
#     print(f"Sorry no staff with {target} salutation.")

# import time
# import winsound

# seconds = int(input("Please enter number of seconds : "))

# hours = seconds//(60*60)
# mins =(seconds//60) % 60  # 0 if temp_mins < 0 else temp_mins # TENARY OPERATOR
# seconds = seconds%60

# # print(hours, mins, seconds)

# end = 0
# interval = -1

# while True:

#     while True:

#         while True:

#             if seconds == end:
#                 break
            
#             seconds += interval
#             print(hours, "hours :", mins, "mins :", seconds, "secs")
#             time.sleep(0.01)

#         seconds = 60
#         if mins == end:
#             break

#         mins += interval

#     mins = 60
#     if hours == end:
#         break

#     hours += interval

# winsound.Beep(1000, 500)
# time.sleep(0.1)
# winsound.Beep(1000, 500)
# time.sleep(0.1)
# winsound.Beep(1000, 500)
# time.sleep(0.1)
# winsound.Beep(1000, 500)

# word = "i am a boy"

# for index, i in enumerate(word):

#     print(index, "-", i)

# x, y = (20, 30)

# print(x, y)

# for x, y, z in [(1,2,3), (4,5,6), (7,8,9)]:

    # print(x, y, z)


# for i in reversed(range(60)):
#     for j in reversed(range(60)):
#         for k in reversed(range(60)):
#             print(i, "hour", j, "min", k, "secs")
#             time.sleep(0.001)


# seconds = int(input("Please enter number of seconds : "))

# hours = seconds//(60*60)
# mins =(seconds//60) % 60  # 0 if temp_mins < 0 else temp_mins # TENARY OPERATOR
# seconds = seconds%60

# for i in reversed(range(hours+1)):
#     for j in reversed(range(mins+1)):
#         for k in reversed(range(seconds+1)):
#             print(i, "hour", j, "min", k, "secs")
#             time.sleep(0.001)
#         seconds = 60
#     mins = 60

# seconds = int(input("Please enter number of seconds : "))

# hours = seconds//(60*60)
# mins =(seconds//60) % 60  # 0 if temp_mins < 0 else temp_mins # TENARY OPERATOR
# seconds = seconds%60

# for i in reversed(range(hours+1)):
#     for j in reversed(range(mins+1)):
#         for k in reversed(range(seconds+1)):
#             print(i, "hour", j, "min", k, "secs", end="")
#             time.sleep(1)
#             # print("\r", end="")
#         seconds = 60
#     mins = 60

# for i in "adamu":
#     print("hello", i)

# oloture_sub = open("files/Oloture.2019.WEBRip.x264-FGT-English.srt", "r")
# counter = 1

# print(oloture_sub.read())
# print(len(oloture_sub.readlines()))

# for line in oloture_sub.readlines():
    
#     if "forze speciali" in line.lower():
#         print("Found in line - ", counter, " - ", line)

#     counter += 1
# print(counter)
        


# names = ["sule", "kunle", "saheed"]


# MAP REDUCE FILTER


# MAP USAGE
# MAP DOES NOT NEED TO BE IMPORTED 

# SALUTE ALL PEOPLE IN LIST


# names = ["sule", "kunle", "saheed"]

# function_to_map = lambda name: "Mr. " + name # CREATE ANONYMOUS FUNCTION USING LAMBDA

# mapped = map(function_to_map, names) # MAP ANONYMOUS FUNCTION TO LIST OF NAMES

# print((mapped))

 # SALUTE USING FOR LOOPS

# names = ["sule", "kunle", "saheed"]
# empty_list = []

# for name in names:
#     empty_list.append("Mr. " + name)

# print(empty_list)

# CLASS WORK

# WRITE A PROGRAM TO CALCULATE GIVE OUT A NEW LIST CONTAINING THE DAILY SALES BELOW AS PERCENTAGES OF THE DAILY TARGET BELOW.

##############################
######## USING FOR MAP  ######
##############################

# daily_sales = [23, 54, 31, 90, 34]
# daily_target = 97

# sales_percentage = map(lambda sale: f"{round(sale/daily_target*100, 2)}%", daily_sales)

# print(list(sales_percentage))


##############################
####### USING FOR LOOPS ######
##############################

# sales_percentages = []

# for sale in daily_sales:
#     sales_percentages.append(f"{round(sale/daily_target*100, 2)}%")

# print(sales_percentages)

# # REDUCE USAGE
# # REDUCE NEEDS TO BE IMPORTED 

# import functools
# # OR
# from functools import reduce

# daily_sales = [23, 54, 31, 90, 34]

# reduction_value = reduce( lambda x, y: x-y*10 , daily_sales)
# print(reduction_value)


# x = ["ab", "we", "as"]
# print(list(map(str.upper, x)))

# FILTER USAGE
# FILTER DOES NOT NEED TO BE IMPORTED 

# daily_sales = [23, 54, 31, 90, 34]

# results = filter(lambda x: x < 10, daily_sales )
# print(list(results))


## DO COLLECTION OF VALUES JUST ONCE 

# value = input("Please enter values to input : ")
# value_to_integer = float(value)

# print(value_to_integer)

## DO COLLECTION OF VALUES JUST OVER AND OVER

# while True:
        
#     value = input("Please enter values to input : ")
#     value_to_integer = float(value)

#     print(value_to_integer)


## DO COLLECTION OF VALUES JUST OVER AND OVER THEN CREATE A LIST WITH COLLECTED NUMBERS

# values_list = []

# while True:
        
#     value = input("Please enter values to input : ")
#     value_to_integer = float(value)

#     values_list.append(value_to_integer)

#     print(values_list)

# DO COLLECTION OF VALUES JUST OVER AND OVER THEN CREATE A LIST WITH COLLECTED NUMBERS ADD A BREAK POINT
# import math

# values_list = []

# while True:
        
#     value = input("Please enter values to input : ")

#     if value.lower() == "q":
#         break

#     value_to_integer = float(value)
#     values_list.append(value_to_integer)
#     print("\nNumbers collected : ", len(values_list), "\n")

# print(values_list)
# number_of_samples = len(values_list)

# mean_of_numbers = sum(values_list)/number_of_samples
# print("\nMEAN : ", mean_of_numbers)


# x_xbar_map = map(lambda sample: round(sample-mean_of_numbers, 2), values_list)
# x_xbar_values = list(x_xbar_map)
# print("\nX_XBAR : \n", x_xbar_values)

# x_xbar_squared_map = map(lambda sample: round(sample**2), x_xbar_values)
# x_xbar_sqaured_values = list(x_xbar_squared_map)
# print("\nX_XBAR_SQUARED : \n", x_xbar_sqaured_values)

# variance = math.sqrt(sum(x_xbar_sqaured_values)/(number_of_samples - 1))
# rounded_variance = round(variance, 2)
# print("\nVARIANCE : \n", rounded_variance)

# file = open("assignment.csv", "w")
# file.write("VALUE,X_XBAR,X_BAR_SQ\n")

# print(f"{('VALUE').center(6)} | {('X_XBAR').center(6)} | {('X_BAR_SQ').center(6)}")
# print("-"*24)
# for i in range(number_of_samples):

#     print(f"{str(values_list[i]).center(6)} | {str(x_xbar_values[i]).center(6)} | {str(x_xbar_sqaured_values[i]).center(6)}")

#     file.write(f"{values_list[i]},{x_xbar_values[i]},{x_xbar_sqaured_values[i]}\n")



for i in range(100,999):
    number_multipied_by_three = i * 3
    last_digit = str(i)[2]*3

    print(i, number_multipied_by_three, last_digit, number_multipied_by_three == int(last_digit))

    if number_multipied_by_three == int(last_digit):
        break