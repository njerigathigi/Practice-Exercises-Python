# exercise Question 8: Generate a Python list of all the even numbers between 4 to 30

def even_numbers_list(data):
    
    even_list = [ number for number in range(data)  if number % 2 == 0 and 4<= number < 30 ]
    print(even_list)

even_numbers_list(50)

print(list(range(4, 30, 2)))
