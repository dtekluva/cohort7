# import datetime

# file_name = "C:/Users/kboys/OneDrive/Desktop/COHORT 3B7 WEEKEND/datastructures/financials.csv"
# file = open(file_name, "r") # OPEN FILE IN READ MODE

# data = file.readlines() # READ FILE LINES 
# data.pop(0) # REMOVE THE FIRST LINE WHICH IS THE HEADER

# ["January"
# "February"
# "March"
# "April"
# "May"
# "June"
# "July"
# "August"
# "September"
# "October"
# "November"
# "December"]
# result_dict = {} # empty dictionary to contain the values on collection
# # print(result_dict.keys())


# #####  THIS PART ONLY RECORDS THE FINAL VALUES FOR EACH MONTH BECAUSE IT REPLACES THE OLD VALUES EVERYTIME.

# # for transaction in data: # LOOP THROUGH ALL THE TRANSACTIONS

# #     split_transactions = transaction.split(",") # split individual transactions in individual values
    
# #     date = datetime.datetime.strptime( split_transactions[3], "%m/%d/%Y") # convert string date to python date object
# #     month_name = date.strftime("%B") # get actual month name in text format
    
# #     transaction_amount = split_transactions[6]
# #     transaction_amount_as_number = float(transaction_amount) # covert transaction amount to decimal number

# #     result_dict[month_name] = transaction_amount_as_number #  APPEND THE AMOUNT TO THE DICTIONARY WITH CORRESPONDING MONTH NAME.

# # print(result_dict)

# for transaction in data: # LOOP THROUGH ALL THE TRANSACTIONS

#     split_transactions = transaction.split(",") # split individual transactions in individual values
    
#     date = datetime.datetime.strptime( split_transactions[3], "%m/%d/%Y") # convert string date to python date object
#     month_name = date.strftime("%B") # get actual month name in text format
    
#     transaction_amount = split_transactions[6]
#     transaction_amount_as_number = float(transaction_amount) # covert transaction amount to decimal number

#     if month_name in result_dict.keys():
#         result_dict[month_name] += transaction_amount_as_number #  APPEND THE AMOUNT TO THE DICTIONARY WITH CORRESPONDING MONTH NAME.
#     else:
#         result_dict[month_name] = transaction_amount_as_number #  APPEND THE AMOUNT TO THE DICTIONARY WITH CORRESPONDING MONTH NAME.

# # print(result_dict)

# # GET HEIGHEST AND LOWEST MONTHS TRANSACTIONS

# # print(result_dict.items())
# values_list = list(result_dict.items())
# # print(values_list)
# values_list.sort(key=lambda val: val[1])
# print(values_list[0]) # LOWEST MONTH
# print(values_list[-1]) # HIGHEST MONTH




import datetime

file_name = "C:/Users/kboys/OneDrive/Desktop/COHORT 3B7 WEEKEND/datastructures/financials.csv"
file = open(file_name, "r") # OPEN FILE IN READ MODE

data = file.readlines() # READ FILE LINES 
data.pop(0) # REMOVE THE FIRST LINE WHICH IS THE HEADER

# month_names = ["January",
#         "February",
#         "March",
#         "April",
#         "May",
#         "June",
#         "July",
#         "August",
#         "September",
#         "October",
#         "November",
#         "December"]

# result_dict = dict.fromkeys(month_names, 0) # empty dictionary to contain the values on collection
# print(result_dict.keys())


#####  THIS PART ONLY RECORDS THE FINAL VALUES FOR EACH MONTH BECAUSE IT REPLACES THE OLD VALUES EVERYTIME.

# for transaction in data: # LOOP THROUGH ALL THE TRANSACTIONS

#     split_transactions = transaction.split(",") # split individual transactions in individual values
    
#     date = datetime.datetime.strptime( split_transactions[3], "%m/%d/%Y") # convert string date to python date object
#     month_name = date.strftime("%B") # get actual month name in text format
    
#     transaction_amount = split_transactions[6]
#     transaction_amount_as_number = float(transaction_amount) # covert transaction amount to decimal number

#     result_dict[month_name] = transaction_amount_as_number #  APPEND THE AMOUNT TO THE DICTIONARY WITH CORRESPONDING MONTH NAME.

# print(result_dict)

# for transaction in data: # LOOP THROUGH ALL THE TRANSACTIONS

#     split_transactions = transaction.split(",") # split individual transactions in individual values
    
#     date = datetime.datetime.strptime( split_transactions[3], "%m/%d/%Y") # convert string date to python date object
#     month_name = date.strftime("%B") # get actual month name in text format
    
#     transaction_amount = split_transactions[6]
#     transaction_amount_as_number = float(transaction_amount) # covert transaction amount to decimal number

#     if month_name in result_dict.keys():
#         result_dict[month_name] += transaction_amount_as_number #  APPEND THE AMOUNT TO THE DICTIONARY WITH CORRESPONDING MONTH NAME.
#     else:
#         result_dict[month_name] = transaction_amount_as_number #  APPEND THE AMOUNT TO THE DICTIONARY WITH CORRESPONDING MONTH NAME.

# print(result_dict)

# GET HEIGHEST AND LOWEST MONTHS TRANSACTIONS

# print(result_dict.items())
# values_list = list(result_dict.items())
# # print(values_list)
# values_list.sort(key=lambda val: val[1])
# print(values_list[0]) # LOWEST MONTH
# print(values_list[-1]) # HIGHEST MONTH


# GET MONTHLY DIFFERENCE
# previous_month_name = "Non"
# previous_month_amount = 0

# for month, amount in result_dict.items():
#     # print(month, amount)

#     print(previous_month_name, month, amount - previous_month_amount)
#     previous_month_name = month
#     previous_month_amount = amount

    

#WRITE EACH COMPANY'S TAXES INTO INDIVIDUAL FILES

file_name = "C:/Users/kboys/OneDrive/Desktop/COHORT 3B7 WEEKEND/datastructures/financials.csv"
file = open(file_name, "r") # OPEN FILE IN READ MODE

data = file.readlines() # READ FILE LINES 
data.pop(0) # REMOVE THE FIRST LINE WHICH IS THE HEADER
destination_path = "C:/Users/kboys/OneDrive/Desktop/COHORT 3B7 WEEKEND/company data"

for transaction in data: # LOOP THROUGH ALL THE TRANSACTIONS

    split_transactions = transaction.split(",") # split individual transactions in individual values
    company_name = split_transactions[5]
    # print(split_transactions[5])

    company_file = open(f"{destination_path}/{company_name.replace('/', '-')}.csv", "a")
    company_file.write(transaction)
    company_file.close()