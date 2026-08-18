from math import *
from random import *
#1) operators
a=10
b=3

print(a+b)
print(a-b)
print(a*b)

#division:- always returns a float no matter operands are int/float 
print(a/b) #3.33
print(4/2) #2.0
#floor division: removes the decimal point just keep the int
print(a//b) #3
print(7//2) #3

print(a%b)

print(2**3) #power

print("------2------")
#2) comparison operators
x = 10

print(x == 10)   # True
print(x != 10)   # False
print(x > 5)     # True
print(x <= 10)   # True

print("-----3------")
#3) assignment operators 
x = 10

x += 5    # x = x + 5 → 15
x -= 3    # x = x - 3 → 12
x *= 2    # x = x * 2 → 24


print("-----4------")

#4) Math library functions

print(abs(-10)) #returns absolute value no sign 10

#round rounds to higher if .5 or greater and lower in if less than .5 returns an int by default


print(round(3.5))
print(round(3.4))

#round to fixed decimal
print(round(3.145555,2)) #3.15


#floor:- returns lower int always
print(floor(3.19)) #3

#ceil:- return higher int always
print(ceil(2.1)) #3

print(pow(2,3))


#min and max
print(min(1,2,3))
print(max(1,2,3)) 

# also works on a list 
arr=[1,100,1000]
print(max(arr))


#sum:0 sums all items in iterabale
arr=[1,2,3,4,5]
print(sum(arr))


#square root:- returns a float always
print(sqrt(7))
print(sqrt(4))


print("-------5-----")
# 5) type conversions

a=5.6
b="123"

#for float it return lower int like floor doesnt rounds off
c=int(a)
print(c)
c=int(b)
print(c)


#float:- converts to float

print(float(10))
print(float("123.05"))


print("----------6--------")
#6radom functions
#1) random() returns random float from 0.0 upto 1.0 not including 1
print(random())

# generate single digit int 0-9
print(int(random()*10))

#generate double digit int from 0-99
print(int(random()*100))



#copying an int
a=10
b=a #an object in memory exists which has 10 in it and both a and b point to same memory location

#but if a or b is changed later a new object is created and a or b points to that

# a now points to new data and b still points to a 
a=a+1
a=20
