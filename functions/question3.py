# Exercise Question 3: Write a function calculation() such that it can 
# accept two variables and calculate the addition and subtraction of it. 
# And also it must return both addition and subtraction in a single return call

def calculation(x , y):
    return (x + y), (x- y)

print(calculation(6, 2))

add , substract = calculation(6, 2)
print(add)
print(substract)
