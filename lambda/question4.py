# Using .sort() method, create a lambda function that sorts the list 
# in descending order. Refrain from using the reverse parameter.


# (Hint: lambda will be passed to sort method's key parameter as argument)

lst=[100, 10, 10000, 1, 9, 999, 9]

lst.sort(reverse= False, key= lambda x: 1/x)

print(lst)
