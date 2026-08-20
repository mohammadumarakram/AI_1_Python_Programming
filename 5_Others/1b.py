#different sizez
a = [1, 2, 3, 4]
b = ['x', 'y']

print(list(zip(a, b)))


#unzipping
pairs = [('Alice', 25), ('Bob', 30)]

names, ages = zip(*pairs)

#gives two tuples
print(names)
print(ages)


#creating a dict:- note that use two collections only one for keys and one for values
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

zp=zip(keys,values)
d=dict(zp)
print(d)
