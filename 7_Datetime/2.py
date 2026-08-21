#1) api styles datetime
from datetime import *

#it gives time in curr
curr=datetime.now()
print(curr)

#it gives time in utc and is an object
currUtc=datetime.now(timezone.utc)
print(currUtc)


#make the datetime object into a string
api_date=currUtc.isoformat()
print(api_date) #2026-08-21T09:34:28.873164+00:00 
#.873. is microseconds


#b) iso string to datetime object

#dt is now a datetime object
dt=datetime.fromisoformat(api_date)
print(dt)



#web dev example making a dict

curr=datetime.now(timezone.utc)
to_store=curr.isoformat()
data={
    "name":"umar",
    "loginTime":to_store

}

print(data)
print(type(data["loginTime"]))


#comparing datetimes

# ============================================================
# 19. CHECK TOKEN EXPIRATION
# ============================================================

created_at = datetime.now(timezone.utc)

expires_at = created_at + timedelta(hours=1)

if datetime.now(timezone.utc) >= expires_at:
    print("Token expired")
else:
    print("Token is valid")

#4) cache expiration
# ============================================================
# 20. CACHE EXPIRATION
# ============================================================

cached_at = datetime.now(timezone.utc)

cache_lifetime = timedelta(minutes=10)

if datetime.now(timezone.utc) - cached_at > cache_lifetime:
    print("Cache expired")
else:
    print("Use cached data")
    