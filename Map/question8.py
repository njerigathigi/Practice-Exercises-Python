# Write a Python program to convert a given list of integers and 
# a tuple of integers in a list of strings

num1 = [1, 2, 3]
num2 = (4, 5, 6)

result = list(map(str, num1))
result1 = list(map(str, num2))
print(result)
print(result1)
   