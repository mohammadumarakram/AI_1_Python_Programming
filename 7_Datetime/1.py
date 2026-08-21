#datetime module it contains multiple classes like datetime, time ,date 
# to use function of a class have to use class.funtion()

#import all classes


from datetime import *

#1) datetime class:- now is a class function it belongs to class datetime not an object

#now is function which creates an actual datetime object so curr is now an datetime object containing current datetime

curr=datetime.now()

#the object internally is like 
# datetime object
# ├── year        → 2026
# ├── month       → 8
# ├── day         → 20
# ├── hour        → 19
# ├── minute      → 42
# ├── second      → 15
# ├── microsecond → 123456


#when using print it converts all properties to string and converts to strings
print(curr)
print(type(curr))


#some methods of datetime object cant access the members directly they maybe private so use functions

print(curr.date())
print(curr.time())


#2) creating a date

# ============================================================
# 2. CREATING A DATE / DATETIME
# ============================================================
#date is also a class like datetime but only contains date 

#like constructor create date object and datetime object 

#pass year,month,day
d = date(2026, 8, 20)
print(d)

#for datetime object pass year,month,day,hr,minute,second
dt = datetime(2026, 8, 20, 19, 30, 15)
print(dt)



#3)getting individual items
#step-1 create a datetime object first using now

curr=datetime.now() #creates an object 
print(curr.year)
print(curr.month)
print(curr.day)
print(curr.hour)
print(curr.minute)
print(curr.second)



#4) convert datetime object to string


# ============================================================
# 4. FORMATTING DATETIME → STRING
# ============================================================

curr = datetime.now()

formatted = curr.strftime("%Y-%m-%d")

print(formatted)
# 2026-08-20


formatted = curr.strftime("%d/%m/%Y %H:%M:%S")

print(formatted)
# 20/08/2026 19:30:15


# Common format codes:
#
# %Y = 4-digit year
# %m = month
# %d = day
# %H = hour (24-hour)
# %M = minute
# %S = second
# %A = weekday name
# %B = month name




# ============================================================
# 5. STRING → DATETIME
# ============================================================

text = "2026-08-20 19:30:00"

#dt is a datetime object now
dt = datetime.strptime(text, "%Y-%m-%d %H:%M:%S")

print(dt)
print(dt.year)


#6 adding and subtracting date

curr=datetime.now()
#by adding and subtracting also it returns a datetime object

#timedelta is also anobject which represnets difference
tomorrow=curr+timedelta(days=1)
yesterday=curr-timedelta(days=1)

future=curr+timedelta(days=3,hours=5,minutes=20)


#7) time difference

start = datetime(2026, 8, 20, 10, 0)
end = datetime(2026, 8, 20, 15, 30)

#diff is a timedelta object
diff=start-end ## 5:30:00 

print(diff.total_seconds())
# 19800.0


#8 comparing dates
# ============================================================
# 8. COMPARING DATES
# ============================================================

today = date.today()

deadline = date(2026, 12, 31)

if today < deadline:
    print("Deadline has not arrived")

if today == deadline:
    print("Today is the deadline")

#9) timestamp

curr=datetime.now()
#Also, timestamp() is giving you the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) its float
tstamp=curr.timestamp()


#converting timestamp back to datetime object pass a timestamp in it

dt=datetime.fromtimestamp(tstamp)


#10) UTC time

ut=datetime.now(timezone.utc)
print(ut)
#2026-08-21 07:32:10.475153+00:00 datetime in utc time 00:00 means offset

#also a datetime object only



#11) expiry

#expire after 30 minutes
expire=datetime.now()+timedelta(minutes=30)

curr=datetime.now()

if curr<expire:
    print("not expired")
else:
    print("expired")


#12) gap in years

birth=date(2003,5,21)
today=date.today()
print(today)

#age is timedelta object
age=today.year-birth.year
print(age)


# ============================================================
# 15. GET WEEKDAY
# ============================================================

today = date.today()

print(today.weekday())

# Monday = 0
# Tuesday = 1
# ...
# Sunday = 6