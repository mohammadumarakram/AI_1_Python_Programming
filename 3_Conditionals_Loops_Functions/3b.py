#1) positional arguements
#arguements are matched by the order of input when calling
def student(name,age):
    print(name,age)

student("umar",23)

#2) keyword arguements

def student(name, age):
    print(name)
    print(age)

#order doesnt matter and keyword is not a string
student(age=22, name="Umar")

#default arguement:- if nor arguement is passed it uses the default value or else the input
def greet(name="User"):
    print("Hello", name)

greet() #user
greet("Umar") #umar


# 3) *args :- if i dont know how many inputs will be passed

#numbers is a tuple here
def sum(*numbers):
    sum=0
    for x in numbers:
        sum+=x

    return sum

print(sum(1,2,3,4,5))


#4) kwargs:- if you dont know number of keyword arguements from before

# arguement  becomes a dictionary

def student(**details):
    # details is a dict 
    for key,value in details.items():
        print(f"{key}-{value}")


#the keywrod becomes a string instead
# details = {
#     "name": "Umar",
#     "age": 28,
#     "school": "iisj"
# } 
student(name="Umar",age=28,school="iisj")



#5) functions as a variable
def greet():
    print("Hello")

x = greet

x()


#6) passing function as argument
def square(x):
    return x * x

def calculate(function, number):
    return function(number)

print(calculate(square, 5))


#7) lambda functions
# lambda input: returned output

square= lambda x:x*x

sum= lambda a,b:a+b

print(sum(5,10))

    


#8) map function: map(function,iterable data structure) it applied the function to each element of DS dont use () after funtion

# map(function,iterable1,iterable2..)
#Note:- function must return something
#returns a map object of results convert to list

l=[1,2,3,4]

mp=map(lambda x:x*x, l)

lst=list(mp)
print(lst)


#using inbuilf function dont use ()
#convert string to int
nums = ["10", "20", "30"]

result = map(int, nums)

print(list(result))

#using normal function
def greet(name):
    return f"Hello, {name}!"

names = ["Alice", "Bob", "Charlie"]

result = map(greet, names)

print(list(result))

#multiple iterables 
a = [1, 2, 3]
b = [4, 5, 6]

result = map(lambda x, y: x + y, a, b)

print(list(result))

#applies only to certain elements

l=[1,2,3,4]

#map will return for each element wont skip any
mp=map(lambda x: x*x if x%2==0  else x, l)

lst=list(mp)
print(lst)




#9) filter:- keep only elements you want and the function must return true/false also returns map object
#filter(function,iterable)
l=[1,2,3,4,5]

mp=filter(lambda x: True if x%2==0 else False,l)
lst=list(mp)
print(lst)

# now can apply map on even number from the filtered list
mp=map(lambda x:x*x,lst)






