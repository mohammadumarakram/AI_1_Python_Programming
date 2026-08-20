
#truthy and falsy

# Falsy values 
#  bool,int float :-  False,0,0.0
#  string,list,tuple,dict,set= "",[],(),{},set() if any of them is empty

#rest all are truthy 

str=""

# if str is not empty
if str:
    print("not empty")
else:
    print("empty")

#if str is empty
if not str:
    print("not empty")
else:
    print("empty")




# if with strings 

name="Mohammad Umar"

if name=="Mohammad Umar":
    print("yes")

if "Umar" in name:
    print("yes")


# if with lists 
fruits = ["apple", "banana", "mango"]

if "apple" in fruits:
    print("Apple is available")


#ternary operator
#x=value if true else value2 (if false)
marks=90
result= "Pass" if marks>30 else "fail"