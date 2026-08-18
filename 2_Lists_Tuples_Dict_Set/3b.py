d = {
    "name": "Umar",
    "age": 22,
    "marks": [85, 90, 78],
    "address": {
        "city": "Delhi",
        "country": "India"
    },
   
}


#looping
for key in d.keys():  # can do like in d also
    print(key)


print("----")
for value in d.values():
    print(value)

print("----")
for key,value in d.items():
    print(key,value)



#length:- number of items
print(len(d))


print("-D---------------")
#copiying:- refers to same dict
a={"age":23}
b=a
b["age"]=25
print(a)

# modified orignal a also

#to create a separate dict
a={"age":30}
b=a.copy()

b["age"]=100
print(a)
print(b)


print("-----E---------")
#creating dict from keys
lst=["a","b","c"]
d=dict.fromkeys(lst,0) #0 default to all keys
print(d)

print("-----F---------")
#dict comprehension:- used in numbers both key and value is int/float
d={x:x*x for x in range(5)}
print(d)

d = {x: x*x for x in range(10) if x % 2 == 0}


# Nested dict 
users = {
    "user1": {
        "name": "Umar",
        "age": 22
    },
    "user2": {
        "name": "Ali",
        "age": 25
    }
}

print(users["user1"]["name"])
# Umar
for user_id, data in users.items():
    print(user_id)
    print(data["name"])
    print(data["age"])


# dict with lists 
d = {
    "names": ["Umar", "Ali", "Ahmed"],
    "marks": [80, 90, 85]
}
print(d["names"][0])
# Umar
