#any:any() → True if at least one value is truthy.
values = [False, False, True]

print(any(values))
# True


#all :- True if every value is truthy.
values = [True, True, True]

print(all(values))
# True


any() and all()

# Both expect one iterable as input, such as a list, tuple, set, etc. They look at the elements and return a Boolean (True or False).

#generator expression
numbers = [2, 4, 6, 8]

print(all(x % 2 == 0 for x in numbers))
# True
# all(function) the func is applied to each element of the collection and returns either true or false 
