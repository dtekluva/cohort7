# file = open("datastructures/financials.csv", "r")

# # print(file.readline()[12:20]) # GET TAX TYPE VIA SLICING

# # heading_list = file.readline().split(",")

# # print(heading_list)
# # print(heading_list[5])

# cash_transactions = []

# for line in file.readlines():

#     transaction_type = line.split(",")[7]

#     if transaction_type == "Own Bank Che...":
#         print(line.split(",")[5], line.split(",")[8])


#####################
#### DICTIONARIES####

## CREATING DICTIONARIES ##

# DIRECT CREATION

# MY_DICT = {
#     "john":["singing", "dancing"],
#     "ali":["jumping", "dancing"],
#     "simbi":["ten ten", "eating"]
# }

# print(MY_DICT)

# scores = {
#     "math": 90,
#     "english":77,
#     "physics": 68
# }

# print(scores)

# names = ["samuel", "lucas", "mary"]
# ages = [34, 21,19]


# print(list(zip(names, ages)))

my_dict = dict() # empty dictionaries can be created using the dict builtin function
# new_dict = (dict(zip(names, ages))) # dictionaries can also be created using a list of list or list of tuples
# print(new_dict)

# print(my_dict)
# print(list(enumerate(names)))

# UPDATING DICTIONARIES

# print(my_dict)

# my_dict["laptops"] = ["hp", "acer", "dell", "toshiba"]
# my_dict["phones"] = ["apple", "samsung", "nokia"]
# my_dict["sneakers"] = ["nike air", "jordans", "jeezy's", 12]
# my_dict[12] = "INVALID ..OOUPS..!!!"

# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# UPDATING DICTIONARY VALUES

import datetime

# print(datetime.date.today())
# print(datetime.datetime.now())

time_now = datetime.datetime.now()

# print("day : ", time_now.day, " Day name : ", time_now.strftime("%A"))
# print("month : ", time_now.month)
# print("year : ", time_now.year)
# print("hour : ", time_now.hour)
# print("min : ", time_now.minute)
# print("second : ", time_now.second)
# print("micro : ", time_now.microsecond)

# print(time_now.strftime("%A"))
# print(time_now.strftime("%b %d, %Y %I:%M%p")) # (-STRPTIME()-) CONVERT TIME FROM DATE OBJECT TO STRING FORMAT OF CHOICE

# sample_date = "2020-20-12"

# print(datetime.datetime.strptime(sample_date, "%Y-%d-%m").strftime("%b %d, %Y %I:%M%p"))

# single add

# bio_dict = dict()

# name = input("Please enter your name : ")
# age = input("Please enter your age : ")
# small_talk = input("Please enter a small talk : ")

# time_created = datetime.datetime.now().strftime("%b %d, %Y %I:%M%p")

# bio_dict[name] = {
#     "age": age,
#     "small_talk": small_talk,
#     "time_created": time_created
# }

# # print(name, age)
# # print(small_talk)
# # print("created at : ", time_created)
# print(bio_dict.values())
import pprint

bio_dict = dict()

while True:

    name = input("Please enter your name : ")
    age = input("Please enter your age : ")
    small_talk = input("Please enter a small talk : ")

    time_created = datetime.datetime.now().strftime("%b %d, %Y %I:%M%p")

    bio_dict[name] = {
        "age": age,
        "small_talk": small_talk,
        "time_created": time_created
    }

    action = input("Please do you want to add another ?? y/n : ")
    if action == "n":
        break

# print(name, age)
# print(small_talk)
# print("created at : ", time_created)
pprint.pprint(bio_dict)