#1) strings
name = "Umar"

for char in name:
    print(char)

name = "Umar"

for i in range(len(name)):
    print(name[i]) 

#2) lists
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

fruits = ["apple", "banana", "mango"]

for i in range(len(fruits)):
    print(i, fruits[i])

# using enumerate
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
    print(fruits[index])
# it gives index and element both in case need to do something with index 

#start with index 1
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

#reversed loop 
numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number)

#2d Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for number in row:
        print(number)
    

#3) tuples
numbers = (10, 20, 30, 40)

for number in numbers:
    print(number)


# unpacking loop 
t=[(1,2),(3,4)]

for x,y in t:
    print(x,y)

#4) set
numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)
# Remember: sets are unordered, so don't depend on the order in which elements are printed.


#5) dict
student = {
    "name": "Umar",
    "age": 22,
    "marks": 85
}

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)


