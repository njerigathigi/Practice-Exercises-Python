# Write a Python program to square the elements of a list using map() function. 

even_numbers = [2, 4, 8, 10]

squared_numbers = list(map(lambda x : x ** 2, even_numbers))
print(squared_numbers)
