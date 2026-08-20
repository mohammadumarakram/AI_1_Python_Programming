# 1) for loop 

#range(start,end,step size) if start not defined takes from 0 and end is not included default step size +1
for i in range(5):
    print(i)

print("------A-------")
for i in range(1,11):
    print(i)

print("------A-------")

for i in range(1,10,2):
    print (i)

print("------B---------")
#printing reverse
for i in range(10,0,-1):
    print(i)


#break:breaks the whole loop
for i in range(10):
    if i == 5:
        break

    print(i)


#continue skips that iteration
for i in range(5):
    if i == 2:
        continue

    print(i)


#for loop with else
for i in range(5):
    print(i)
else:
    print("Loop finished")
# else executes after loop is finished and if break is used its not executed
