# Using sorted() function and lambda sort the words in the list based 
# on their second letter from a to z.

lst=["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]

lst = sorted(lst, key = lambda x : x[1])
print(lst)
