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

