#Integers

x = 13
y = -3

#Floating-Point Numbers

pi = 3.14159
radius = 2.5

#Complex Numbers

z = 3 + 4j

#Strings

name = "Paulo Oliveira"
message = 'Hello, Paulo!'

#String concatenation

greeting = "Hello"
name = "Paulo"
full_greeting = greeting + " " + name
print(full_greeting)  # Output: Hello Paulo

#Booleans

is_raining = True
is_sunny = False

#Lists

numbers = [1, 2, 3, 4, 5]
fruits = ["orange", "strawberry", "banana"]
mixed_list = [5, "banana", False, 3.14]

#List Access

print(fruits[0])  # Output: orange

#Lists are mutable

fruits[0] = "guava"
print(fruits)  # Output: ['guava', 'strawberry', 'banana']

fruits.append("grape")
print(fruits)  # Output: ['guava', 'strawberry', 'banana', 'grape']

fruits.remove("banana")
print(fruits)  # Output: ['guava', 'strawberry', 'grape']

#Tuples

person = ("Paulo", 39, "Portugal")

#Tuples Access

print(person[0])  # Output: Paulo

#Sets

fruits = {"apple", "banana", "strawberry", "banana"}
print(fruits)  # Output: {'strawberry', 'banana', 'apple'}

#Set Operations

set1 = {1, 2, 3}
set2 = {2, 3, 4}

union = set1 | set2
print(union)  # Output: {1, 2, 3, 4}

intersection = set1 & set2
print(intersection)  # Output: {2, 3}

difference = set1 - set2
print(difference)  # Output: {1}

#Dictionaries

student = {"name": "Paulo", "age": 39, "grade": "A"}


#Dictionaries Access

print(student["name"])  # Output: Paulo

#Dictionaries are mutable

student["grade"] = "B"
print(student)  # Output: {'name': 'Paulo', 'age': 39, 'grade': 'B'}

student["country"] = "Portugal"
print(student)  # Output: {'name': 'Paulo', 'age': 39, 'grade': 'B', 'country': 'Portugal'}

del student["age"]
print(student)  # Output: {'name': 'Paulo', 'grade': 'B', 'country': 'Portugal'}
