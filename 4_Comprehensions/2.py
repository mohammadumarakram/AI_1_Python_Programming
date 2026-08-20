#dictionary comprehensions:- make a new dict from an existing collection can be anything list tuple etc

lst=[1,2,3,4,5]

#create dict with {x:x square}
#x means each element in lst and key:value of dict can use x or anything else also  not lambda function
d={x:x*x for x in lst}
# print(d)

#with condition only if
#keep even numbers only
d={x:x*x for x in lst if x%2==0}
# print(d)

#with conditon if else
#square even and for odd use 1 default
d={x:x*x if x%2==0 else 1 for x in lst}
# print(d)



#put discount on each price
# Transform an existing dictionary
prices = {
    "apple": 100,
    "banana": 50,
    "orange": 80
}

new_prices={x:0.9*(y) for x,y in prices.items()}
# print(new_prices)


#filter a dictionary:- keep only items with price>50
new_items={x:y for x,y in prices.items() if y>50}
print(new_items) 
