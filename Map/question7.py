#  Write a Python program to add two given lists and find the difference 
#  between lists. Use map() function.
num1 =[1, 2, 3]
num2 =[4, 5, 6]
def sum_and_diff(x, y):
    return x + y, x - y
    
summation = list(map(sum_and_diff, num1, num2))
print(summation)
