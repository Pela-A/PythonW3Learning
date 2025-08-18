# Scope refers to variables and their availability based on region created

def myfunc():
    x = 298
    print(x)

myfunc()

# the scope of x is local of myfunc

# Functions inside functions can access that variable x
def myfunc():
    x = 299
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

# Variables created in the main body of code are considered to have global scope
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# If you have two variables that belong to differnt scope, the function will use local scope while outside the function global scope will be used
x = 300

def myfunc():
    x = 200
    print(x)

myfunc()
print(x)

# Use global keyword inside local scope to create global variables
def myfunc():
    global x
    x = 500

myfunc()

print(x)

# Use global keyword to change a global scope variable inside local scope (different since we were creating a global scope variable versus modifying)
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

# nonlocal keyword is used to make variables belong to outer function

# If in a nested function i define a variable the same name as parent function, using non local makes it reference outer function scope instead of inner
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
    print(x)
  print(x)
  myfunc2()
  print(x)
  return x

print(myfunc1())
# With nonlocal gone, setting x to hello in myfunc2() would only modify x in the myfunc2() and not x in myfunc1()