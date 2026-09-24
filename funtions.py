#basic function
def greet():
    print("hello")
    print("welcome to python")

#function without parameters
def welcome():
    print("welcome to python")

welcome()
welcome()  

#function with parameter
def greet(name):
    print("hello",name)

greet("bhargavi")
greet("ravi") 

#multiple parameters
def add(a,b):
    print("sum:",a+b)

add(10,20)
add(50,30)    

#funtion with return value
def add(a,b):
    return a + b

result = add(10,20)

print(result)

#function for even/odd
def check_even_odd(number):

    if number % 2 == 0:
        print( "even")
    else:
        print( "odd")


result = check_even_odd(25)        

# Function for Pass or Fail

def check_pass_fail(marks):
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")

check_pass_fail(75)
check_pass_fail(35)

#function for largest of two numbers
def largest(a,b):

    if a>b:
        return a
    else:
        return b


result = largest(50,30)

print("largest:",result)

#function +user input
def square(number):
    return number * number


number = int(input("enter number:"))

result = square(number)

print("square:", result)

#function +loop
def multiplication_table(number):

    for i in range(1,11):
        print(number,"x",i,"=",number*i)



number = int(input("enter number:"))

multiplication_table(number) 

#add two numbers
def add(a,b):
    return a + b

x = int(input("enter first number:"))
y = int(input("enter secound number:"))

result = add(x, y)
print("sum =",result)

#even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

num = int(input("enter a number:"))

print(check_even_odd(num))

#largest of three numbers
def largest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>= a and b>= c:
        return b
    else:
        return c 

a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))

print("largest =",largest(a,b,c))

#grade caluculation
def find_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

marks = int(input("enter marks:"))

print("grade =",find_grade(marks))






