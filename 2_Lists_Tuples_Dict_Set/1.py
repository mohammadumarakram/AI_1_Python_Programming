#List:- like array but can contain different data types not just fixed and also its dynamic in nature can grow later not fixed size so more like vector in c++ 

# also they are mutable original list can be changed

list=[1,2,3]
list2=[1,2,"Umar",7.98]
l=[] #empty list


#1) accessing elements
#indexing 0,1,2
print(list[0]) 

#returns new list
print(list[1:3]) #start,end not including end
print(list[:3]) #upto index 3
print(list[2:]) # start from index 2 till end 


#2) adding element at last
list.append(50)
list.extend([100,200]) # adds multiple items at once
b=[100,200]

#can add another list elements also
list.extend(b)
list.insert(1,99) #inserts 99 at first index
print(list)


print("----------2-----------")
#3) removing elements
l=[1,2,3,4,5]
a=l.pop() #removes and returns last element
print(l.pop(1)) #removes element at an index and returns it

#remove:- removes first occurance of the element does not return it
l=[10,10,20,30]
l.remove(10)
print(l)

#clear:- empties the list
l.clear()


print("---------3----------")
#searching and counting
l=[1,2,3,4,5,5]
print(l.index(1)) #index of first occc of 1
print(l.count(5)) #count of 5

#if x is present in list
print(2 in l)
print(2 not in l)

print("---------3----------")

a=[1,2,3]
print(len(a))

#sort in ascending order and modifes orignal no new return 
a.sort()
a.sort(reverse=True) #descing order

#reverse:- modifes orginal
a.reverse()

#copying
b=a.copy()

# b=a is invalid its like refernce variable the list exisits in memory and now both a and b point to it only no new list is created


#looping through value

#indexing 0-(len(list)-1)
#range(start,end,step size) end is not included
lst=[1,2,3,4,5]
for x in lst:
    print(x)

for i in range(len(lst)):
    print(lst[i])

#indexing from any i
for i in range(1,len(lst)):
    print(lst[i]) 

#indexing with step size of 2
for i in range(1,len(lst),2):
    print(lst[i])

#indexing backward
#start=last index end=-1 not 0 because then 0 will not be included and reduce 1
for i in range(len(lst)-1,-1,-1):
    print(lst[i])



print("-------5-------")
# list comprehension 
a=[1,2,3,4,5]
b=[x*2 for x in a] #[1,4,9,16,25]

c=[x*2 for x in a if x%2==0] #[4,16]

