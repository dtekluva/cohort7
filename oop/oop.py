# class Employee: # class definition

#     name = "Ade"
#     age = 23
#     salary = 230000

#     def get_salary(self):
        
#         return self.salary

# new_employee = Employee() #instance or object creation
# print(new_employee.name)
# print(new_employee.get_salary())

# class Admin(Employee): #Admin employee inheriting from Employee

#     # # name attribute and get salary method have been altered via the concept of polymorphism. 
    
#     name = "kunle"
#     designation = "Human resources"
#     vat = 0.05

#     def get_salary(self):
#         return (self.salary *1.5 ) - (self.salary*self.vat)

# second_employee = Admin() #instance or object creation
# print(second_employee.age)
# # print(second_employee.name)
# # print(second_employee.designation)
# # print(second_employee.get_salary())

# adminpeople = [Admin() for i in range(30000)]
# ordinarypeople = [Employee() for i in range(30000)]

# print(adminpeople[0])


# class special_str(list):
    
#     def upper(self):
#         return "Gbabge  awa o se mo..!!"
#     def last(self):
#         return self[-1]


# x= special_str("johana")
# # q = x.upper()
# print(x.last())

class Employee:

    def __init__(self, name, last_name, age, salary):

        self.name = name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    def describe(self):
        print(f"Name : {self.name} {self.last_name}")
        print(f"Age : {self.age}")
        print(f"Salary : {self.salary}\n")

names = ["John", "salami","kunle", 'segun', "chima", "nedu", "obi", "tosin", "tolu", "hassan", "abba"]

import random

employees= [Employee(name = random.choice(names), 
                        last_name = random.choice(names),
                        age = random.randint(20, 80),
                        salary = random.randint(35000, 450000)
                    )
                for i in range(len(names))
            ]

# employees[0].describe()

for employee in employees:
    employee.describe()