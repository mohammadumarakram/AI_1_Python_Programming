#zip function
#zip() is a built-in Python function that combines elements from two or more iterables (such as lists, tuples, or strings) into  a single tuple

#it returns a collection of tuples inside an object so if iterate gives individual tuple


#if collection 1 has lesser elements than collection 2 it stops producing combinations till shorter one

l1=[1,2,3]
l2=["umar","rehan","akram"]

zp=zip(l1,l2)

#convert the zip object into a list which contains multiple tuples of combinations
lst=list(zp)
print(lst)



l1=[1,2,3]
l2=["umar","rehan","akram"]
l3=[100,200,300]

zp=zip(l1,l2,l3)

#convert the zip object into a list which contains multiple tuples of combinations
lst=list(zp)
print(lst)



#looping though it 
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
    