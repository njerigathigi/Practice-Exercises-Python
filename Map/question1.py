# Write a Python program to triple all numbers of a given list of integers. 
# Use Python map

numbers = [1, 2, 3, 4, 5]

print(list(map(lambda x: x * 3, numbers))) #returns a new iterator that yields transformed items on demand.
