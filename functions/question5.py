# Exercise Question 5: Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it


def func1( a, b):
    addition = lambda a , b : a + b

    return (addition(a , b) + 5 )



print(func1(4, 4))

def outerfunction(a , b):
    def innerfunction():
        return a + b
    return ( innerfunction() + 5 )

print(outerfunction(4,4))
