#functions

def greet():
    print("hello")

greet()

#no function type or return type
def greet(name):
    print(f"hello {name}")
greet("umar")

def add(a,b):
    return a+b


print(add(3,4))


#2) passing string
name = "Umar"

def greet(name):
    print("Hello", name)

greet(name)
#the original refernce is passed
def change(x):
    x = "Ali"

name = "Umar"
change(name)

print(name)   # Umar
# x is just a local variable string which points to original string but later is assigned to different 

#3) lists
#its also refernce to same object so modification affects original also
numbers = [1, 2, 3]

def change(x):
    x.append(4)

change(numbers)

print(numbers) #1234


# x points to new orignal list but is later reassigned
def change(x):
    x = [10, 20]

numbers = [1, 2, 3]
change(numbers)

print(numbers)

#Note:- if you use reassign using = the local variable creates a new object and points to it, whehter string list or anything but if any function is used like append a[i]=x then original is changed

#same for dictionary,tuple set anything can be passed normally no need to speocfy return or arguement type

