file = open("datastructures/financials.csv", "r") # OPEN FILE INTO PYTHON
file_lines = file.readlines() # READ LINES FROM FILE AS A LIST CONTAINING EACH LINES
file_lines.pop(0) # REMOVE FIRST LINE WHICH IS THE HEADING AND NOT NEEDED

cash_transactions = []

target_company = "CHI LIMITED"
total = 0

for line in file_lines:

    transaction_type = line.split(",")[7] 
    company_name = line.split(",")[5]
    amount_paid = float(line.split(",")[6])

    if company_name == target_company: # LOOK OUT FOR SPECIFIC COMPANY NAME

        total += amount_paid
        # print(company_name, amount_paid)

print(target_company, " : \nTotal ==> ", total)

file.close()

####################################
######                         #####
###   GET UNIQUE COMPANY NAMES   ###
######                         #####
####################################

all_company_names = []


for line in file_lines:

    company_name = line.split(",")[5]
    
    all_company_names.append(company_name)

mylist = all_company_names
myset = set(mylist)


cash_transactions = []

target_company = "CHI LIMITED"
total = 0

####################################
######                         #####
###    GET INDIVIDUAL AMOUNTS    ###
######                         #####
####################################

all_company_names = []

for line in file_lines:

    company_name = line.split(",")[5]
    
    all_company_names.append(company_name)

mylist = all_company_names
myset = set(mylist) # REMOVES DUPLICATES FROM ALL COMPANY NAMES GIVES UNIQUE COMPANY 

for target_company in myset:
    
    total = 0
    for line in file_lines:

        transaction_type = line.split(",")[7] 
        company_name = line.split(",")[5]
        amount_paid = float(line.split(",")[6])

        if company_name == target_company: # LOOK OUT FOR SPECIFIC COMPANY NAME

            total += amount_paid

    print(target_company, " : \nTotal ==> ", total)



