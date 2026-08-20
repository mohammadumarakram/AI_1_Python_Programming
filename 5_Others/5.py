#unpacking
# Unpacking means taking values from a collection and assigning them to separate variables.

numbers = [10, 20, 30]

a,b,c=numbers
#a=10,b=20..


#tuples
person = ("Umar", 28)

name, age = person

print(name)  # Umar
print(age)   # 28


#get first value separate and rest in other using *
#* converts into list
numbers = [10, 20, 30, 40, 50]

a,*rest = numbers

print(a)     # 10
print(rest)  # [20, 30, 40, 50]


#in functions
numbers = [10, 20, 30]

def add(a, b, c):
    return a + b + c

print(add(*numbers))
# add(10, 20, 30)



#with dict:- used to create a new dictionary
# Here **user means:

# Take all key-value pairs from this dictionary and put them here not create w new dict just do key=value for all

user = {"name": "Umar", "age": 28}
extra = {"city": "Delhi"}

result = {**user, **extra}

print(result)
# {'name': 'Umar', 'age': 28, 'city': 'Delhi'}



#with function
user = {
    "name": "Umar",
    "age": 28
}

def show_user(name, age):
    print(name, age)

show_user(**user)
#it becomes keyword arugement type
# show_user(name="Umar", age=28)


