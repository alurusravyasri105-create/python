print("hello class")
age=int(input("enter a age:"))
if(age>=18):
    print("eligible for vote")
    print("eligible for bike ride")
else:
    print("not eligible for vote")
    print("eligible for bike ride")
print("enter your name")

number=int(input("enter a number:"))
if(number==1):
    print("mrd")
elif(number==2):
    print("mbu")
elif(number==3): 
    print("gitam") 
else:
    print("select another collage") 

    number=int(input("enter a number"))
    if(number>0):   
        if(number<50):  
            print("number in between 1-50")
        else:
            print("number is greater than 50")
    else:
        print("-ve number")    

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

#print numbers from 10 to 1
for i in range(10,0,-1):
    print(i)    

#print even numbers from 2 to 50
for i in range(2,51,2):
    print(i)

 #print odd numbers from 1 to 50
for i in range(1,51,2):
    print(i)

#print("multiple of 5 from 5 to 50:")
for i in range(5,50,55):
    print(i)

#multiplication table
number = int(input("enter number:"))

for i in range(1,11):
    print(number,"*",i,"=",number*i)

#sum of numbers from 1 to n
n = int(input("enter n:")) 

total = 0

for i in range(1,n+1):
    total=total+i

print("sum:",total)    

#factorial of a number
n = int(input("enter number:"))

factorial = 1

for i in range(1,n+1):
    factorial = factorial * i

print("factorial:",factorial) 

#sum of even numbers from 2 to n
n = int(input("enter n:"))

total = 0

for i in range(2,n+1,2):
    total = total + i
print("sum;",total)   

#count of multiples of 3
n = int(input("enter n:"))

count = 0

for i in range(1,n+1):
    if i % 3 == 0:
        count = count + 1

        print("count:",count)

#sum of multiples of 5
# n = int(input("enter n:"))

total = 0

for i in range(1,n+1):
    if i % 5 == 0:
        total = total + i

print("sum:",total)   

#print all even numbers from 2 to 50
i = 2
 
while i <= 50:
    print(i)
    i = i+2  

#print all odd numbers from 1 to 50   
i = 1

while i<=50:
    print(i)
    i = i+2

#print total of the numbers by user until 0 is entered
total = 0

number = int(input("enter number:"))

while number != 0:
    total = total + number
    number = int(input("enter number:"))

    print("total:",total) 

#password check
password = ""

while password != "python123":
    password = input("enter password:")

print("login successful")  

#count the number of digits in a number
number = int(input("enter number:"))
count = 0

while number > 0:
    number = number // 10
    count = count + 1

print("number of digits:",count)  

#sum of digits in a number
number = int(input("enter number:"))

total = 0

while number >0:
    digit = number % 10
    total = total + digit
    number = number // 10

print("sum of digits:",total)  

#reverse the number
number = int(input("enter number:"))

reverse = 0

while number >0:
    digit = number % 10
    number = number //10
    reverse = reverse * 10 + digit

    print("reverse:",reverse)

#check if a number is a palindrome
number = int(input("enter number:"))

original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print("palindrome")
else:
    print("not palindrome")    

#check if a number is prime number
number = int(input("enter number:"))

count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count = count + 1

if count == 2: 
    print("prime number")
else:
    print("not a prime number") 

             
# Print all prime numbers between 2 and 100
for number in range(2, 101):

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count = count + 1

    if count == 2:
        print(number)

