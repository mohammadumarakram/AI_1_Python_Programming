#enumerate:- like zip it also creates a tuple or a pair of (index,value)

# [(0, 'apple'), (1, 'banana'), (2, 'orange')] like this then indiviudal iteration gives each element

fruits = ["apple", "banana", "orange"]

for x,y in enumerate(fruits):
    print(x,y)


#starting from different number 
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


#use case
#find the element and return its index
numbers = [10, 20, 30, 40]

for i, num in enumerate(numbers):
    if num == 30:
        print(f"Found at index {i}")
    