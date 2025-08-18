# Add imports to top of code ideally and then utilize functions etc in code

import mymodule

mymodule.greeting("Jonathan")

print(mymodule.randomConstant)

a = mymodule.person1["age"]
print(a)

import mymodule as mx

a = mx.person1["age"]
print(a)

# Python has many built in modules. Basically anything is possible with modules
# With platform you can see your system 
import platform

x = platform.system()
print(x)

# use dir() function to see all function names and variable names in a module
import platform

x = dir(platform)
print(x)


y = dir(mx)
print(y)


# From keyword can be used to import specific components of a module
from mymodule import person1

# Make sure to refer to the elements you imported not the module mymodule.person1["age"] is bad
print (person1["age"])