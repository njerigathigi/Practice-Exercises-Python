# Exercise Question 4: Create a function showEmployee() in such a way that it should 
# accept employee name, and it’s salary and display both, and if the salary is missing 
# in function call it should show it as 9000

#default value functions

def showEmployee(name , salary = 9000):
    
    print("{0}'s salary is ksh {1}.".format(name, salary))

showEmployee('Fiona', 1000000)
showEmployee('Fiona')
