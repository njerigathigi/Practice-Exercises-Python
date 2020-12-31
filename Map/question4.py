import math
# Write a Python program to create a list containing the power of said number in bases 
# raised to the corresponding number in the index using Python map.

numbers = [1, 2, 3, 4, 5]
index = [i for i in range(len(numbers))]
print(numbers)
print(index)

powers = list(map(math.pow, numbers, index))
print(powers)
