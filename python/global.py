# Variables created outside of a function are considered global

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


# If defining a variable locally, it will use the local value over global
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# Define a variable as global scope instead of local
def myfunc():
  global y
  y = "fantastic"

myfunc()

print("Python is " + y)


# Change a global variable inside a function like so
z = "awesome"

def myfunc():
  global z
  z = "wicked"

myfunc()

print("Final: Python is " + z)