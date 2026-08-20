#comprehension
#A comprehension is simply a shorter way to create a new collection from an existing iterable. existing data → process/filter each item → create new collection


# store=[] or {} what ever new Ds you want

#store on all elements
#[value for x in iterable]

#store some elements
# [x for x in iterable if x conditon true]

#use if-else 
#for statement later
# [value if x is true else value(if false) for x in iterable ]
#1) list

# syntax: [value (to put in new list) for x in list if____]
lst=[1,2,3,4,5]

#create a new list of even numbers from l
even=[x for x in lst if x%2==0]
print(even)

#square of all elements
square=[x*x for x in lst]
#square of all even elements 
square=[x*x for x in lst if x%2==0]

#type2:- if else 

#square even and keep odd as it is
# [value_if_true if condition else value_if_false for x in iterable]

square=[x*x if x%2==0 else x for x in lst]



# Transform strings
#convert strings to uppercase
names = ["umar", "ali", "john"]

upper=[x.upper() for x in names]


#wuth dict
# Common in API/data processing:
#get names of users whose greater than 18
users = [
    {"name": "Umar", "age": 28},
    {"name": "Ali", "age": 17},
    {"name": "John", "age": 25}
]

eligible=[x["name"]  for x in users if x["age"]>18]
print(eligible)
