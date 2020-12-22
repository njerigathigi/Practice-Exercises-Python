# Write a Python program to add three given lists using Python map and lambda

numbers = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]
numbers3 = [11, 12, 13, 14, 15]

summation = map(lambda x, y, z: x + y + z, numbers, numbers2, numbers3)
print(list(summation))
