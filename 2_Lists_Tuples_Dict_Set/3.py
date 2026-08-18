#dictioanry:- its a data structure that stored key:value pairs like in a mapping
#also mutable original can be modifed
#1) declaring
d={
    "name":"umar",
    "age":21,
    "city":"delhi"

}

#data type of key:value, value can be any data type possible but keys can be a data type which is immutable not mutable ones like dictionary,list or set 

d = {
    "name": "Umar",       # string → string
    "age": 22,            # string → int
    10: "hello",          # int → string
    3.14: [1, 2, 3],      # float → list
    (1, 2): True          # tuple → bool
}


print("----------A--------")
#2) accessing and updating value
d = {"name": "Umar", 
     "age": 22,
     1:[1,2,3]}

print(d["name"])
print(d[1])

#if a key does not exisits the program crashes with an error
# print(d[3])

# a safer way is using get
print(d.get("name"))
print(d.get("noooo","bob")) #if it does not exisit then returns a default value set


#add a new key
d["salary"]=1000

#updating a key if it exisits updates if not exisits creates one
d["name"]="rehan"


#update functins:-expects a dictionary in input if keys exist will update if not will create
# You can add/update multiple values:
d.update({
    "age": 24,
    "city": "Delhi"
}) 


#merge using update
d1={"name":"umar","age":23}
d2={"salary":1000}
d1.update(d2)
print(d1)



print("--------C------")
#removing a pair:- Removes the key and returns its value.

d = {"name": "Umar", "age": 22}

#pop removes and returns the value also
x = d.pop("age")

# del d["name"] no return just delete

print(x)   # 22
print(d)   # {"name": "Umar"}


#checking if a key exisits:- checks keys not values
print("name" in d)

#check if a value exisits
print("Umar" in d.values())


print("-------D----")
d = {
    "name": "Umar",
    "age": 22,
    "marks": [85, 90, 78],
    "address": {
        "city": "Delhi",
        "country": "India"
    },
   
}

#all keys:- it returns a view view is a live representation of exisitnng keys in that dict its not a separate data object just a representation can also be looped over
print(d.keys())
#convert the view to list
l=list(d.keys())
print(l)

#now can loop over
for x in l:
    print(x)

print(d.values())
print(list(d.values()))

#returns a view of all key values
print(d.items())


