#string methods with different Data structures
print("------1------------")
#split:- converts a string to list of strings
#by default it takes a whitespace as separator even if multiple spaces doesnt matter wont print extra space
s="apple banana    mango"
print(s.split())

#separating using comma
s="apple,mango,banana"
a=s.split(",")
print(a)


print("---------2-------------") 
#2) isdigit,isalpha these also works on strings only but checks the content of a string
"123".isdigit() #not data type int just that string is a numer
# True

"Hello".isalpha()
# True

"Hello123".isalnum()
# True

print("---------3-------------")

#3) join:- converts an iterable list tuple etc to a single string inbetween.join(data structure) the inbetween is what comes in between the elements an empty space or - anything

arr=["hello","how","are","you"]

str=" ".join(arr)
print(str)

dat=["01","05","2026"]
str="-".join(dat)
print(str)

