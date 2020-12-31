# Write a Python program to convert all the characters in uppercase and 
# lowercase and eliminate duplicate letters from a given sequence. Use map() function

letters = ['A', 'b', 'c', 'D', 'c', 'e']

def to_upper_lower(char):
    return char.upper(), char.lower()

lettrs =set(map(to_upper_lower, letters))
print(lettrs)
