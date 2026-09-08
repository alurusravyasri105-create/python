#arthimethic operations

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("power:", a ** b)

#simple caluculator
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#student marks calculator
name = input("Enter the student's name: ")

m1 =int(input("Enter python marks: "))
m2 =int(input("Enter java marks: "))
m3 =int(input("Enter sql marks: "))

total = m1 + m2 + m3
average = total / 3

print("\n----- student report -----")
print("Name:", name)
print("Total Marks:", total)

#shopping bill caluculator
price1 = float(input("Enter the price of item 1: "))
price2 = float(input("Enter the price of item 2: "))
price3 = float(input("Enter the price of item 3: "))

total = price1 + price2 + price3

discount = total * 0.10
final_amount = total - discount

print("Discount:", discount)
print("Final Amount to be paid:", final_amount)
print("total bill:", total)
print("Thank you for shopping with us!")

#comparison operators
a = 10
b = 20

print("a == b:", a == b)
print("a != b:", a != b)
print("a < b:", a < b)
print("a > b:", a > b)
print("a <= b:", a <= b)
print("a >= b:", a >= b)

#assignment operators
x = 10

x +=5
print(x)

x -= 2
print(x)

x*= 3
print(x)

#bank balance
balance = 10000

deposite = 500
balance += deposite

print("Updated balance:", balance)

withdraw = 2000
balance -= withdraw

print("after withdraw balance:", balance)

#pass or fail checker
marks = int(input("Enter your marks: "))

print("passed:", marks >= 40)
print("failed:", marks < 40)

#login validation
correct_username = "admin"
correct_password = "1234"

username = input("Enter your username: ")
password = input("Enter your password: ")

print(username == correct_username) 
print(password == correct_password)

# Setup variables
age = 20
has_id = True
is_suspended = False

# 1. AND Example (Both must be True)
if age >= 18 and has_id:
    print("Eligible to enter the venue.")

# 2. OR Example (At least one must be True)
if age < 12 or age >= 65:
    print("Eligible for a special discount.")

# 3. NOT Example (Inverts a condition)
if not is_suspended:
    print("Account is active and eligible to participate.")

# Combining all three together
# Priority order: 'not' evaluates first, then 'and', then 'or'
if (age >= 18 and has_id) and not is_suspended:
    print("Access fully granted!")
    
  #electricity bill calculator
units = int(input("enter electricity units: "))

rate = 6

bill = units * rate

print("Electricity bill:", bill)

#BITWISE OPERATORS
a = 5
b = 3

print(a & b) #bitwise AND
print(a | b) #bitwise OR
print(a ^ b) #bitwise XOR

#identity operaters
a = None

print(a is None)
print(a is not None)

#travel expence caluculator
travel =float(input("Enter travel expenses: "))
food = float(input("Enter food expenses: "))
hotel = float(input("Enter hotel expenses: "))

total = travel + food + hotel

print("Total expenses:", total)

#student scholarship eligibility checker
marks = float(input("Enter your marks: "))
attendance = float(input("Enter your attendance: "))

eligible = marks >= 85 and attendance >= 75

print("scholarship eligible:", eligible)

#atm eligibility checker
balance = 1000
withdrawal_amount = 5000

print(withdrawal_amount > 0 and withdrawal_amount <= balance) 

#logical operators
age = 25
citizen = True

print(age >= 18 and citizen ==True)