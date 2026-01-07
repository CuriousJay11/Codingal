# sets
basketball = {"vijay", "arnav", "rohan", "saksham", "arghya", "rahul", "hem", "dhoni", "jadeja", "sachin"}
chess = {"vijay", "gita", "bhavna", "saksham", "ravi", "raghav", "dhoni", "renuka", "sachin", "vishal", "rajesh"}

print(basketball)
print(chess)

print(type(basketball))

# combined both the sets and gave the unique items
print(basketball.union(chess))

# common people
print(basketball.intersection(chess))

# who like playing basketball but do not like playing chess
print(basketball.difference(chess))

# who like playing chess but do not like playing basketball
(print(chess.difference(basketball)))

# who like only playing one sport
(print(basketball.symmetric_difference(chess)))
