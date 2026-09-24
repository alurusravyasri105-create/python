#list in python
# list is an ordered and changeable collection  that can store multiple items in a single variable
import numbers


mark = [80, 90, 75, 85]

print(mark)

#accessing elements in a list
marks = [80, 90, 75, 85]

print(marks[0])
print(marks[1])
print(marks[2])


#change element in a list
marks = [80, 90, 75]

marks[1] = 95

print(marks)

#add element to a list
marks = [80, 90, 75]

marks.append(85)

print(marks)

#remove element from a list
marks = [80, 90, 75,]

marks.remove(90)

print(marks)

#insert element in a list
numbers = [10, 20, 30]

numbers.insert(1,15)

print(numbers)

a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)

print(a)

numbers = [20, 20, 30, 20]

numbers.remove(20)
print(numbers)

numbers = [20, 20, 30, 20]

numbers.clear()
print(numbers)

numbers = [10, 20, 30, 40]

print(numbers.index(30))

numbers = [10, 20, 20, 30, 20]

print(numbers.count(20))

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

numbers.sort(reverse=True)

print(numbers)

numbers = [10 ,20 ,30 , 40]

numbers.reverse()

print(numbers)

a = [1, 2, 3]

b = a.copy()

print(b)

numbers = [10, 20, 30, 40 ,50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
print(numbers[::-5])
print(numbers[ -1::])
print(numbers[::-2])
print(numbers[::-4])
print(numbers[-3::])
print(numbers[4:5])

 #tuple in python
 #tuple is a collection of multiple values that is ordered and cannot be changed after creation
student = ("sravya", 95 , "python")

print(student[0])

#access values in a tuple

student = ("sravya", 21,85.5)

print(student[0])
print(student[1])
print(student[2])


#tuple are immutable,meaning they cannot be changed after they are created.they are defined using parenthasis
numbers = (10, 20, 20, 30, 20)

print(numbers.count(20))

numbers =(10, 20, 30, 40)

print(numbers.index(30))

numbers = (10, 20, 30, 40)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#sets in python
#set is a collection of unique values that is unordered and mutable
numbers = {10, 20, 30, 20, 10}

print(numbers)

#addnvalues to a set
subjects = {"python","java"}

subjects.add("sql")

print(subjects)

#remove values from a set
subjects.remove("java")

print(subjects)

#sets do not allow duplicate values
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)

#dictionaries in python
#dictionary is a collection of key-value pairs that is unordered and mutable
student = {
    "name":"sravya",
    "age":17,
    "course": "python"
}

print(student)

#access elements in dic
print(student["name"])
print(student["age"])
print(student["course"])

#add new data to a dictionary
student["city"] = "tirupathi"

print(student)

student = {
    "name": "sravya",
    "age": 17,
    "course": "python"
}
print(student.values())
#values()returns all the values in the dictionary

print(student.items())
#items()returns all key-valu pairs

print(student.get("name"))
#get()returns the value of the specified key

student.update({"age":22})
#update()updates the value of the specified key

print(student)

student.pop("age")
#pop()removes the specified key and its values

print(student)

#popitem()removes the last inserted key-value pair
student = {
    "name": "sravya",
    "age": 17,
    "course": "python"
}

student.popitem()

print(student)

student = {
    "name":"sravya"
}
student.setdefault("age", 17)

print(student)

number = int(input("enter a number"))

if number % 5 == 0:
    print("divisible by 5")

# temperature check
temperature = float(input("enter temperature:"))

if temperature > 40:
    print("high temperature")   

marks = int(input("enter marks:"))

if marks >= 40:
    print("pass")
else:
    print("fail")

number = int(input("enter a number:"))

if number >=0:
    print("positive")
else:
    print("negative")

number = int(input("enter a number:"))

if number > 100:
    print("number is greater than 100")
else:
    print("number is not greater than 100")

marks = int(input("enter marks:"))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")   

a = int(input("enter first number:"))
b = int(input("enter secound number:"))

if a > b:
    print("largest:",a)
elif b > a:
    print("largest:",b)
else:
    print("both are equal")

a = int(input("enter first number:"))
b = int(input("enter secound number:"))
c = int(input("enter third number:"))  

if a >= b and a>= c:
    print("largest:", a)
elif b >= a and b>= c:
    print("largest:", b)
else:
    print("largest:", c)  

number = int(input("enter a number:"))

if number > 0:
    print("positive")
elif number < 0:
    print("negative") 
else:
    print("zero")       

day = int(input("Enter weak number"))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thrusday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("invalid")

a = float(input("enter first number:"))
b = float(input("enter secound number:")) 
operator = input("enter operator(+,-,*,/):")

if operator == "+":
    print("result",a+b)
elif operator =="-":
    print("result",a-b)
elif operator =="*":
    print("result",a*b)
elif operator =="/":
    if b != 0:
        print("result",a/b)
    else:
        print("cannot divide by zero")
else:
    print("invalid operator")

username = input("enter username:")  
password = input("enter password:")

if username == "admin":
    if password == "1234":
        print("login successful")
    else:
        print("wrong password")
else:
    print("wrong username")

balance = float(input("enter balance:"))
amount = float(input("enter withdrawl amount:"))

if amount >0:
    if amount <= balance:
        balance = balance - amount
        print("witdrawl successful")
        print("remaining balance:",balance)
    else:
        print("insufficient balance")
else:
    print("invalid amount")           

marks = int(input("enter marks:"))
attendance = float(input("enter attendance percentge:"))                

if marks >= 40:
    if attendance >=75:
        print("eligible")
    else:
        print("not eligible due to attendance")
else:
    print("fail") 

age = int(input("enter age:"))
test = input("did you pass the driving test?(yes/no):")

if age >=18:
    if test == "yes":
        print("licence can be issued")
    else:
        print("pass the driving test first")
else:
    print("not eligible due to age")    

#order of evalution 
print(2+13*2)

result = (10+5)*2
print(result)

#for loop

#used to repeat code or iterate through a sequence.

for i in range(1, 6):
    print(i)

#use while when repetition depends on a condition.
#looping through numbers 1 to 5 using while loop
i = 1

for i in range(1,11):
    print(i) 

#find the largest number among 5 numbers entered by the user
largest = None   

for i in range(5):

    number = int(input("enter number:"))

    if largest is None or number > largest:
        largest = number

print("largest:",largest)



