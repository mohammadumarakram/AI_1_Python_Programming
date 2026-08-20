#important use cases
# ============================================================
# 7) COMMON API/AI DATA CLEANING
# ============================================================

# Remove empty values

data = ["Umar", "", "Ali", None, "John"]

clean = [x for x in data if x]
# ['Umar', 'Ali', 'John']


# Extract a field from API response

users = [
    {"id": 1, "name": "Umar"},
    {"id": 2, "name": "Ali"},
    {"id": 3, "name": "John"}
]

names = [user["name"] for user in users]
# ['Umar', 'Ali', 'John']


# Create an ID → user dictionary

users_by_id = {
    user["id"]: user
    for user in users
}

