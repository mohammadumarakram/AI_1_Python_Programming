#set comprehensions 
s={1,2,2,3,4,5,5}
#set is unordered and removes duplicates when you iterate
# print(s)

news={x*x for x in s}
# print(news)

news={x*x for x in s if x%2==0}
news={x*x if x%2==0 else 0 for x in s }
#{0,4,0,16,0} but since its set it removes duplicates
# print(news)



# Useful when you need unique values.
# For example, unique roles from API data:

users = [
    {"name": "Umar", "role": "admin"},
    {"name": "Ali", "role": "user"},
    {"name": "John", "role": "admin"}
]

#{admin,user,admin} but will remove duplicate
unique={x["role"] for x in users}
print(unique)
