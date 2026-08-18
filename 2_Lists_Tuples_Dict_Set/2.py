# tuples:- A tuple is like a list, but immutable: once created, you cannot change, add, or remove its elements. but it can be resassigned to new tuple it can also contain multiple data types

t=(1,2,3,"umar")
print(t)
t=(1,2,3,4)
t=() #empty
t=(1,) #comma is required for single element or else it becomes an int


print("---------A------")
t=(11,22,33,44,55,66)
print(t[0])
#(start,end) returns a new tuple 
print(t[0:3])

print(len(t)) #return number of elements


print("--------B------")
for x in t:
    print(x)
for i in range(0,len(t)):
    print(t[i])

print("--------C------")

print(22 in t)
print(2 in t)



print("--------D-----")
#unpacking separating elements and assigning them into variables
t = (10, 20, 30)

a, b, c = t

print(a)    # 10
print(b)    # 20
print(c)    # 30

print("--------E-----")

#builtin functions
len(t)       # number of elements
min(t)       # smallest
max(t)       # largest
sum(t)       # sum

#this return a list not tuple
lst=sorted(t)    # returns a NEW list

print("--------F-----")
#converion to list
l=[1,2,3]
t=(1,2,3)

#list to tuple 
newTuple=tuple(l)
newTuple=tuple([1,2,3])

#tuple to list
newList=list((1,2,3))






