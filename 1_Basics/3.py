#strings
a="Hello"
b="HI"


#1) accessing chqrachters
#they return new string can print directly
#indexing starts from 0-n-1 and from back to start from -1,-2,-3
a="PubgMobile"
print(a[0])
print(a[-1])
print(a[-2])

#slicing
#[start,end] does not includes end and L-R direction
# +1 each step from start
print(a[0:3])
#-5,-4,-3 its also L-R
print(a[-5:-1])




#[start:] includes start till end all
print(a[1:])
#-3,-2,-1 its also L-R
print(a[-3:])


#[:end] from start 0- end-1 does not includes end

print(a[:4])
print(a[:-1])

print("------------1-------")



#2) concatenation:- no extra space by default
print(a+b)
c="HI "+"Umar "+ a
print(c)

#3) len:- number of chars

a="Hello"
print(len(a))