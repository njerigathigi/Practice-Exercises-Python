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

showStudent = displayStudent
    

showStudent('Fiona', 26)
