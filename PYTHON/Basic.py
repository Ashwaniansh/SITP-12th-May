
# # name="ashwani"
# # print(name.capitalize())
# # company_name = "Ansh  "
# # print(len(company_name))
# # print(company_name.strip())
# # company_name = "Ansh"  Indexing
# # print(company_name[-1])
# # company_name = "Ashwani"
# # print(company_name[0:3])
# # Reverse the string
# # name = "Ashwani"
# # last_name = "Kumar"
# # print(name,last_name)
# # print(name * 2)
# # intro = """*Very Important - Final Townhall and Exit Test Intimations*

# # This is to formally inform all *pre-final year students* of the Passing Out Batch 2027 that a Town Hall Meeting is scheduled for all eligible students who wish to participate in the Central Placement Process at the SRM IST KTR ( Main Campus), Chennai. The details of the meeting are as follows:  

# # *Date - 20.05.2026* 
# # *Time -  11:00 AM* 
# # *Venue -  Easwari Auditorium* .

# # Attendance is mandatory as the points discussed here will not be repeated or elaborated on later.  Students who attend this meet will leave with a clear roadmap and a significant advantage as they step into this important phase. 

# # Further, the Exit Test that is deemed Mandatory to avail NoC for placements, both on/off campus placements, will be held on the following dates. 

# # *22.05.2026 — Afternoon Session*

# # *23.05.2026 — Forenoon and Afternoon Sessions*

# # Students are instructed to take note of the above schedule and be prepared."""
# # print(intro)
# # intro ="This is Ashwani Kumar \n Hello Ansh"
# # intro.split("\n","")
# # name = "Ashwani"
# # address = "Madhubani"
# # print(f"my name is {name} and i am from {address}")

# # INPUT FUNCTION
# # name = input("Enter your name:-")
# # print(name)
# # print(type(name))

# # LIST
# # lst = [1,2,3,4,5,"Ashwani",6,7]
# # print("This is my first list:-",lst)
# # print("length of my list:-",len(lst))
# # print("Type of my list:-",type(lst))

# # print = 10
# # print(print)

# # list = 10
# # print(">>>>><><<<<<<",list)

# # lst = [1,2,3,4,5,"Ashwani",6,7]
# # print(lst[0])
# # print(lst[2])
# # print(lst[4])
# # print(lst[3])
# # print(lst[5])
# # print(lst[7])

# # print(lst[-1])



# # print(lst[0:5])
# # print(lst[2:5])
# # print(lst[2:7])


# # operations
# # fruits = ["Apple", "Banana", "Lichi"]
# # add item
# # fruits.append("Orange")
# # fruits.insert(0,"Grapes")
# # fruits.remove("Apple")
# # fruits.pop(1)
# # fruits.clear()
# # fruits.copy()
# # print(fruits.count("Apple"))
# # print(fruits.index("Apple"))
# # fruits[0]="Kiwi"
# # fruits.reverse()
# # print("Fruits list:- ",fruits)


# lst1 = [1,2,3]
# lst2 = [4,5,6]
# print(">>>>>><><<<<<<",2 in lst1)
# print(lst1+lst2)

# Tuple

# tpl1 = (1,2,3,4,"Ashwani",2,2.5,1,2)
# print("This s my first tuple:-",tpl1)
# print("Length of my tuple:-",len(tpl1))
# print(tpl1[0])
# a = 1,2,3,4.5,5,"Ashwani"
# print(a)
# print(type(a))
# print(len(a))

# tuple unpacking(Automatically data divide)
# a,b,c = (1,2,3)
# print(a)
# print(b)
# print(c)

# tpl = (1,2,3,"Ashwani",5,6,7)
# print(tpl)
# print(tpl.count(1))
# print(tpl.index(1))

# Type casting
# tpl = (1,2,3,4,"Ansh",5,6)
# print("Ye mera tpl:-",tpl)
# print("Type of my tuple",type(tpl))

# print("Tuple convert into list",tpl)
# lst = list(tpl)
# print(">>>>",lst)
# print(">>>>",type(lst))
# lst.append(100)
# print(lst)
# tpl = tuple(lst)
# print(tpl)

# Dictionary

# student = {"Name":"Ashwani","Class":"MCA","Rollnumber":2,"Branch":"COMPUTER APPLICATION","Address":"GHAZIABAD"} 
# print(student)
# print("Dict Keys",student.keys())
# print("Dict Values",student.values())
# print("Dict items",student.items()
# print(student['class'])
# print(student['branch'])

# add item in python dict
# student = {}

# student["name"] = "Ansh"
# student["age"] = 20
# student["city"] = "Patna"

# print(student)
# print(student.get('name'))

# student = {
#     "name": "Ashwani",
#     "age": 22,"course":"Python"
# }

# student.clear()
# print(student)
# new_student = student.copy()
# print(new_student)

# student.pop("age")
# print(student)
# student.popitem()
# print(student)
# print(student.get("name"))

# Set default

# car={"Brand":"Mahindra","Model":"XUV","Year":2024}
# x=car.setdefault("color","white")
# print(x)

# car={"Brand":["Mahindra","Tata","Hero","Bajaj"],"Model":"XUV","Year":2024}
# for x in car.items():
#   print(x)
# print(car)
# car['Year']=2025
# print(car)


# Set

# set = {1,2,3,4,5}
# print("This is my first set:-",set)
# print("Type of my first set:-",type(set))
# print("Len of my first set:-",len(set))
# set.remove("2")
# set.discard("1")
# print(set)


# Operators

# x = 15
# y = 4

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)
# print(x ** y)
# print(x // y)

# amount = int(input("Enter order amount: "))
# if amount >= 200:
#     print("Free Delivery Available")
# else:
#     print("Delivery Charges Applied")

# marks = int(input("Enter your marks: "))
# if (marks >= 90 and marks <= 100) or marks == 100:
#     print("Grade: A++")
# elif marks >= 80 and marks < 90:
#     print("Grade: A")
# elif marks >= 70 and marks < 80:
#     print("Grade: B")
# elif marks >= 60 and marks < 70:
#     print("Grade: C")
# elif marks >= 50 and marks < 60:
#     print("Grade: D")
# elif marks >= 40 and marks < 50:
#     print("Pass")
# elif marks >= 0 and marks < 40:
#     print("Fail")
# else:
#     print("Invalid Marks")

# password = input("Enter password: ")
# if len(password) >= 14:
#     if password == "Ashwani@76887.":
#         print("Login Successful")
#     else:
#         print("Wrong Password")
# else:
#     print("Password must contain at least 12 characters")
# class BMICalculator:

#     def calculate_bmi(self):

#         weight = float(input("Enter your weight in kg: "))
#         height = float(input("Enter your height in meters: "))

#         bmi = weight / (height ** 2)

#         print("\nYour BMI is:", round(bmi, 2))

#         if bmi < 18.5:
#             print("Category: Underweight")

#         elif bmi >= 18.5 and bmi < 25:
#             print("Category: Normal Weight")

#         elif bmi >= 25 and bmi < 30:
#             print("Category: Overweight")

#         else:
#             print("Category: Obese")


# # Object Creation
# person = BMICalculator()

# # Function Call
# person.calculate_bmi()
# class ATM:

#     def __init__(self):
#         self.balance = 1000
#         self.pin = "1234"

#     def check_pin(self):
#         entered_pin = input("Enter ATM PIN: ")

#         if entered_pin == self.pin:
#             return True
#         else:
#             print("Incorrect PIN")
#             return False

#     def check_balance(self):
#         print("Current Balance:", self.balance)

#     def deposit(self):
#         amount = float(input("Enter amount to deposit: "))
#         self.balance += amount
#         print("Amount Deposited Successfully")
#         print("Updated Balance:", self.balance)

#     def withdraw(self):
#         amount = float(input("Enter amount to withdraw: "))

#         if amount <= self.balance:
#             self.balance -= amount
#             print("Please collect your cash")
#             print("Remaining Balance:", self.balance)
#         else:
#             print("Insufficient Balance")

#     def menu(self):

#         if self.check_pin():

#             while True:

#                 print("\n===== ATM MENU =====")
#                 print("1. Check Balance")
#                 print("2. Deposit Money")
#                 print("3. Withdraw Money")
#                 print("4. Exit")

#                 choice = input("Enter your choice: ")

#                 if choice == "1":
#                     self.check_balance()

#                 elif choice == "2":
#                     self.deposit()

#                 elif choice == "3":
#                     self.withdraw()

#                 elif choice == "4":
#                     print("Thank You for Using ATM")
#                     break

#                 else:
#                     print("Invalid Choice")


# # Object Creation
# user1 = ATM()

# # Run ATM
# user1.menu()
class BMICalculator:

    def __init__(self):

        self.name = input("Enter Your Name: ")

        while True:

            try:

                self.weight = float(input("Enter Weight (kg): "))
                self.height = float(input("Enter Height (m): "))

                if self.weight > 0 and self.height > 0:
                    break

                else:
                    print("Weight and Height must be greater than 0")

            except ValueError:

                print("Please Enter Numbers Only")

    # Calculate BMI
    def calculate_bmi(self):

        bmi = self.weight / (self.height ** 2)

        return round(bmi, 2)

    # BMI Category
    def bmi_category(self, bmi):

        if bmi < 18.5:

            return "Underweight"

        elif bmi < 25:

            return "Normal Weight"

        elif bmi < 30:

            return "Overweight"

        else:

            return "Obese"

    # Display Result
    def display_result(self):

        bmi = self.calculate_bmi()

        category = self.bmi_category(bmi)

        print("\n===== BMI REPORT =====")

        print("Name :", self.name)
        print("Weight :", self.weight, "kg")
        print("Height :", self.height, "m")
        print("BMI :", bmi)
        print("Category :", category)


# Object Creation
person = BMICalculator()

# Display Result
person.display_result()