# value1 = 20
# value2 = 20

# print("Value 1 is equal value 2 : ", value1 == value2)
# print("Value 1 is less than value 2 : ", value1 < value2)
# print("Value 1 is greater or equal to value 2 : ", value1 >= value2)
# print("Value 1 is less or equal to value 2 : ", value1 <= value2)
# print("Value 1 is not equal to value 2 : ", value1 != value2)

# name = input("Please enter your name : ")
# age = int(input("Please enter your age : "))
# years_of_experience = int(input("Please enter your years of experience : "))

# current_year = 2020
# year_of_birth = current_year - age

# min_allowable_year_of_birth = 1989
# max_allowable_year_of_birth = 2001
# years_of_experience_for_exception = 3

# response = year_of_birth > min_allowable_year_of_birth and \
#             year_of_birth < max_allowable_year_of_birth or \
#             years_of_experience >= years_of_experience_for_exception and \
#             not (years_of_experience > age)

# print("Thank you for applying", name)
# print("You met all criteria : ", response)

# PROGRAM TO CHECK IF A WORD CONTAINS ANOTHER WORD

# word = input("Please enter base word : ")
# other_word = input("Please enter word to check : ")

# print(other_word, "was found : ", other_word in word)

# if "Mr" in word:
#     print("Good day sir")

# elif "Mr" not in word:
#     print("Baba how far..!!")

# word = input("Please enter base word : ")

# print(f"A was found {word}: {'a' in word}")
# print(f"E was found {word}: {'e' in word}")
# print(f"I was found {word}: {'i' in word}")
# print(f"O was found {word}: {'o' in word}")
# print("U was found in", word, " : ", "o" in word)


names = (("ade", 1985), ("bola", 1995), ("johnson", 2001), ("sam", 1994))

for name, year_of_birth in names:

    age = 2020 - year_of_birth
    template = f"Happy birthday {name} you are amazing and we thought of you first today, as you turn {age} today may you be blessed with abundance."
    print(template)

# import requests

# def send_simple_message(email, message):
# 	return requests.post(
# 		"https://api.mailgun.net/v3/mg.oyoyong.com/messages",
# 		auth=("api", ""),
# 		data={"from": "OYOYONG <mailgun@oyoyong.com>",
# 			"to": [email],
# 			"subject": "DATASCIENCE UNIVEL",
# 			"text": message})

# names = (("Damilola", 1995, "arowolodamilola5@gmail.com"), ("Chinedu", 1991, "chijazzconcepts@gmail.com"), ("Queen", 1993, "queen.adiat@gmail.com"), ("Obum", 1994, "obumanichebe@gmail.com"))

# for name, year_of_birth, email in names:

#     age = 2020 - year_of_birth
#     template = f"Happy birthday {name} you are amazing and we thought of you first today, as you turn {age} today may you be blessed with abundance."
#     # print(template)

#     send_simplmdjkbvjdkcfkl;knv.kfkmdflj;ld,jfd;e_message(email, template)

my_text = "ade said \ni am a a boy\""
print(my_text)