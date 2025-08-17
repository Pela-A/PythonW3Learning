# Example implementations
x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared a type, python handles this. Can even change
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Python does allow casting

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))

a = "J"
# is the same as (might be able to have chars as well)
b = 'J'

print(type(a))
print(type(b))

#* Python variable rules
# Variables must start with letters or _
# Variable can't start with numbers
# Variables can only contain alpha-numeric characters and underscores
# variable names are case sensitive
# Variable names can not be python keywords

# Different variable naming conventions

#* Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "John"

#****************
# Multiple values assignment

# Simple
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Assign the same value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpacking values in a collection
fruits = ["apple", "banana", "cherry"]
print(type(fruits))
x, y, z = fruits
print(x)
print(y)
print(z)

#****************
# Variable output

# In example one, a separator is added
# Support different data types
# Print argument separation
x = "Python"
y = "is"
z = "awesome"
print(x, y, z, sep="A")


# String concatenation requires manual spacing
# Note that non strings must be cast as strings
x = "Python "
y = "is "
z = "awesome"
print(x+y+z)

#****************


#****************