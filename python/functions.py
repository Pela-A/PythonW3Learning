# Functions
# Define with def nameOfFunction(params):
def my_function():
  print("Hello from a function")

# Calling functions is normal
my_function()

# Pass information into function as arguments
# Params belong to function signature
def my_function(fname, lname):
  print(fname + " " + lname)

# Arguments
my_function("Emil", "Refsnes")


# Can pass key = value for args so order does not matter
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Can also use the * before a parameter name in a function so it can receive a tuple of arguments (number of args does not matter) known as *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# There is also an option for keyword arguments **.
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Default parameter values are possible too
# If no arg is passed, the default parameter will be used
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Arguments can be any data type, and will be treated the same inside the function

# Returns are standard
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# Empty functions can be declared using pass inside the body of function
def myfunction():
  pass

# Can define a function to only accept positional arguments or keyword arguments
# Positional requires a , / at the end
def my_function(x, /):
  print(x)
my_function(3)

# Keyword arguments only requires *, at the start

def my_function(*, x):
  print(x)

my_function(x = 3)

# ALSO if you are a lunatic, you can use both argument types. Why anyone would do this is beyond me but you can do it
# arguments before /, are positional only, arguments after *, are keyword arguments only
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

# Recursion is allowed in python
# Recursion is like a more complicated for loop that sometimes can be simpler
# Base case/condition that ends
# Recursive case that calls the function
# Some component that moves the function towards the base case

# As recursion runs, the call stack builds up
# When the base case is reached, the stack starts to unwind as we pop off functions/frames off the stack
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    # base case means that k is no longer greater than 0. We return this value and pop from call stack
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)