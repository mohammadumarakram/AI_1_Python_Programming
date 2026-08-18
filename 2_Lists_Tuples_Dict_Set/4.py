# ============================================================
# 1. CREATING SETS:- mutable and not sorted by default there is no fix order even if declared 1,2,3 it can print in any order
# ============================================================

s = {1, 2, 3, 4}

print(s)
# {1, 2, 3, 4}

# Duplicate values are automatically removed
s = {1, 2, 2, 3, 3, 3}
print(s)
# {1, 2, 3}


# ============================================================
# 2. EMPTY SET
# ============================================================

s = set()

print(s)
# set()

# IMPORTANT:
# {} creates an empty dictionary, NOT an empty set.
# ============================================================
# 3. CREATE SET FROM A LIST / STRING / TUPLE
# ============================================================

s = set([1, 2, 2, 3, 4])
print(s)
# {1, 2, 3, 4}

s = set("hello")
print(s)
# {'h', 'e', 'l', 'o'}
# Duplicate 'l' is removed.

s = set((1, 2, 3))
print(s)
# {1, 2, 3}


# ============================================================
# 4. SET IS UNIQUE
# ============================================================

numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)

print(unique_numbers)
# {1, 2, 3, 4}

# Very common use:
# Remove duplicates from a list.

# ============================================================
# 5. ADDING AN ELEMENT - add()
# ============================================================

s = {1, 2, 3}

s.add(4)

print(s)
# {1, 2, 3, 4}

# If the value already exists, nothing happens.

s.add(4)

print(s)
# {1, 2, 3, 4}



# ============================================================
# 6. ADDING MULTIPLE ELEMENTS - update()
# ============================================================

s = {1, 2, 3}

s.update([4, 5, 6])

print(s)
# {1, 2, 3, 4, 5, 6}

# update() can accept another set, list, tuple, etc.

s.update({7, 8})
print(s)

# ============================================================
# 7. REMOVE - remove()
# ============================================================

s = {1, 2, 3, 4}

s.remove(3)

print(s)
# {1, 2, 4}

# IMPORTANT:
# remove() gives KeyError if the element doesn't exist.

# s.remove(10)
# KeyError


# ============================================================
# 8. REMOVE - discard()
# ============================================================

s = {1, 2, 3}

s.discard(2)

print(s)
# {1, 3}

# Unlike remove(), discard() does NOT give an error
# if the element doesn't exist.

s.discard(100)

print(s)
# {1, 3}

# ============================================================
# 10. clear()
# ============================================================

s = {1, 2, 3}

s.clear()

print(s)
# set()


# ============================================================
# 11. LENGTH - len()
# ============================================================

s = {10, 20, 30, 40}

print(len(s))
# 4

# ============================================================
# 12. CHECK IF ELEMENT EXISTS - in
# ============================================================

s = {"Umar", "Ali", "Ahmed"}

print("Umar" in s)
# True

print("John" in s)
# False

if "Umar" in s:
    print("User exists")

# ============================================================
# 13. LOOPING THROUGH A SET
# ============================================================

s = {"Python", "Java", "C++"}

for language in s:
    print(language)

# Order is not guaranteed.


# ============================================================
# 14. UNION - combine two sets
# ============================================================

a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)

print(result)
# {1, 2, 3, 4, 5}

# Shorter syntax:

result = a | b

print(result)
# {1, 2, 3, 4, 5}


# ============================================================
# 15. INTERSECTION - common elements
# ============================================================

a = {1, 2, 3}
b = {2, 3, 4}

result = a.intersection(b)

print(result)
# {2, 3}

# Shorter syntax:

result = a & b

print(result)
# {2, 3}
# ============================================================
# 16. DIFFERENCE
# ============================================================

a = {1, 2, 3}
b = {2, 3, 4}

result = a.difference(b)

print(result)
# {1}

# Means:
# Elements that are in a but NOT in b.

# Shorter syntax:

result = a - b

print(result)
# {1}

# ============================================================
# 22. SET COMPARISON
# ============================================================

a = {1, 2, 3}
b = {3, 2, 1}

print(a == b)
# True

# Order does NOT matter in sets.

print(a != b)
# False


# ============================================================
# 23. SETS DON'T SUPPORT INDEXING
# ============================================================

s = {10, 20, 30}

# print(s[0])
# TypeError

# You cannot do:
# s[0]
# s[1]
#
# because sets are unordered collections.

# 25. SET WITH DIFFERENT DATA TYPES
# ============================================================

s = {1, 2.5, "hello", True}

print(s)

# A set can contain different hashable types.


# ============================================================
# 26. IMPORTANT: SET ELEMENTS MUST BE HASHABLE
# ============================================================

# This works:

s = {1, 2, 3}

# This does NOT work:

# s = {[1, 2], [3, 4]}
# TypeError

# Lists cannot be elements of a set because lists are mutable.
# ============================================================
# 28. COPY A SET
# ============================================================

a = {1, 2, 3}

b = a.copy()

b.add(4)

print(a)
# {1, 2, 3}

print(b)
# {1, 2, 3, 4}


# ============================================================
# 30. MODIFYING SET WITH update()
# ============================================================

a = {1, 2, 3}

a.update({4, 5, 6})

print(a)
# {1, 2, 3, 4, 5, 6}


