# Exercise Question 7: Assign a different name to function and call it 
# through the new name

# Below is the function displayStudent(name, age). Assign a new name
# showStudent(name, age)  to it and call through the new name

# def displayStudent(name, age):
#     print(name, age)

# displayStudent("Emma", 26)
# 
# you should be able to call the same function using

# showStudent(name, age)

def displayStudent(name, age):
    
    print(name, age)

showStudent = displayStudent #assign the name. do not call the function
# A function is given a name when it is defined, but that name can be reassigned to 
# refer to a different object if desired (don't do this unless you mean to!)
# this function can then be called with the new variable as well as with the old one.

showStudent('Fiona', 26)
