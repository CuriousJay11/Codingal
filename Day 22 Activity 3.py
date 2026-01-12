# sets
today = {"vijay", "arnav", "rohan", "saksham"}
yesterday = {"vijay", "saksham", "rahul"}

print(today)
print(yesterday)

print(type(today))

# combined both the sets and give the unique items
print(today.union(yesterday))

# common people
print(today.intersection(yesterday))

# people present today but not yesterday
print(today.difference(yesterday))
