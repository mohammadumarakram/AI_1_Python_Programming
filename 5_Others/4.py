#sorted() sorted() takes an iterable (list, tuple, set, string, etc.) and returns a new list containing the elements in sorted order. Note:- returns new collection doesnt modify original

numbers = [5, 2, 8, 1, 3]

result = sorted(numbers)
#descending order 
sorted(numbers, reverse=True)


#-----------------------------
#key — important for API/AI work

# key tells Python what to use when deciding the sorting order.
#Note:- key is different than dict key it tells python to sort based on something
#key= basically a function which will be used on each element of collection and returns something based on which sorting is done


#sort based on length of string
names = ["Ali", "Umar", "Ahmed", "Mohammed"]

#len function return length of all one by one and then sorted sorts it
result = sorted(names, key=len)

print(result)


#sort based on age
# pass a function in lambda which calculates value for each element based on which sorted sorts
#get_age(Ali)   → 30
# get_age(Umar)  → 25
# get_age(Ahmed) → 28
students = [
    {"name": "Umar", "age": 28},
    {"name": "Ali", "age": 22},
    {"name": "Ahmed", "age": 25}
]

result = sorted(students, key=lambda x: x["age"])

print(result)

#desneig order
result = sorted(
    students,
    key=lambda x: x["age"],
    reverse=True
)

