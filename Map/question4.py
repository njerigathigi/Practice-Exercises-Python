# Write a Python program to create a list containing the power of said number in bases 
# raised to the corresponding number in the index using Python map.

numbers = [1, 2, 3, 4, 5]

def power(numbers):
    for number in range(len(numbers)):
        power = numbers.index(number)
        return lambda number: number ** power

new_numbers_list = list(map(power, numbers))
print(new_numbers_list)
