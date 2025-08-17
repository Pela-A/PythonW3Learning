# Upper case method
a = "Hello, World!"
print(a.upper())

# Lower case method
# Highly useful if receiving string content that might be capitalized differently but mainly wanting to check if the words represented are the same
a = "Hello, World!"
print(a.lower())

env1 = "devtest"
env2 = "Devtest"

if( env1.lower() == env2.lower() ):
    print("Same environment")


# Strip method to remove white space
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


# Replace method replaces string with another
a = "Hello, World!"
print(a.replace("H", "J"))


# Split method returns a list of strings using the separator as the delimiter
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


#####
# Concatenation

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#####
# String formatting

# Python will not automatically interpret a non string type as string unless cast or using F-Strings

# F-String introduced in 3.6

age = 36
txt = f"My name is John, I am {age}"
print(txt)

# The curly braces are placeholders for variables, functions etc


# Modifiers also exist

# In this example we make price a float data type with two decimal places
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Math operations can occur inside placeholders