
#1) lower and upper:- return new string
a="hello"
b=a.upper()
print(b)

a="HOLA"
print(a.lower())

#2) strip:- removes spaces from start and end not in middle and returns new string

c="   HELLO    World  "
print(c.strip())
s="  Umar  "
s.lstrip()   # removes from left
s.rstrip()   # removes from right 

print("---------2---------")

#3)replace:- replaces a single char or a word
#str.replace(word to replace,new word)
s="Hello World How Are you"
print(s.replace("Hello","HI"))
#replaces just one H with G
print(s.replace("H","G",1))

print("------3-----")
# 4) find:- return index of first occurance of a substring if not then -1

s="Hello world"
print(s.find("world"))
print(s.find("wood"))

print("-----4--------------")
# 5)count:- returns occurance of a substring

s="hello hell hllo"
print(s.count("h"))
print(s.count("he"))

print("-----4--------------")

# 6) starts/endswith:- returns true or false if it starts/ends with that substring

s="Hello world How are you"
print(s.startswith("He"))
print(s.startswith("Hello"))

# L-R only not in reverse 
print(s.endswith("uo"))
print(s.endswith("ou"))

print("-----4--------------")

#7) capitalize:- converts only first letter to uppercase
s="hello world how"
print(s.capitalize())

# 8) title() capitalises first word of each word 
print("hello world".title())
# 'Hello World'

print("-5--------")

#9) membership:- returns true/false if substring is present or not same is find() but return true false instead
s="Hello world"
print("wor" in s)
print("world" in s)

print("----7-------")


#fstring:- used to integrate variable name inside a string 
name="umar"
age=25

s=f"My name is {name} and i am {age}"
print(s)




