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