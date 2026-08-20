
age=19
# 1) if -else
if age>18:
    print("eligible")

else:
    print("not")


#can use brackets also
if (age>=18):
    print("Eligible")

print("---------A-----------")
# 2) elif 

if age>18:
    print("")
elif age==18:
    print("")

else:
    print("")

print("---------B----------")
# 3) and/or
age = 25
salary = 50000

if age >= 18 and salary >= 30000:
    print("Eligible")


day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")

#not operator dont use ! just add not ___

age=10

if not age>18:
    print("yes")


# nested ifs 

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")
    




