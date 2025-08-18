# Lambda functions are small anonymous functions in python

# lambda arguments : expression
x = lambda a: a + 10
print(x(5)) # returns 15

# Any number of arguments can be passed
x = lambda a,b : a * b
print(x(5,6)) # returns 30

# Can return a lambda function from a function for more dynamic functions
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11)) # return 22