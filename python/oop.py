# OOP stands for Object-Oriented Programming

# Python is object oriented allowing code to be structured using classes and objects for organization and code reusability

# Code maintainability
# Helps keep your code DRY (Don't Repeat Yourself)
# The DRY principle means you should avoid writing the same code more than once. Move repeated code into functions or classes and reuse it.

# A class defines what an object should look like while an object is an instance created based on that class

# Almost everything in python is considered an object

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)
p2 = MyClass()

print(p1.x is p2.x)

# Python constructor method is written as __init__()
# Parameters inside must be passed

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person(age = 36, name = "John")

print(p1.age)
print(p1.name)

# __str__() method controls what should be returned if the class object is represented as a string ToString()
print(type(p1)) # <class '__main__.Person'>
print(p1) # <__main__.Person object at 0x000002857AAFF190>

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # Implement __str__
  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# Create methods for class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# self parameter is a reference to the current instance of the class. Acceses variables that belong to the class. Actually can be called anything but self is most common

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# Exploring the difference between self.x and x
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


  # Define a class variable. This is shared by all instances of the class
  # self.x is unique to that instance of the class

  # Priority of python is to search for an instance variable and then the class variable
  x = 5
  def setX(self, x):
    self.x = x

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p2 = Person("Alexander", 30)
p1.setX(4)
print(p1.x)
print(p2.x)

#* Deleting
# You can either delete object properties or entire objects

# Age property on p1 Person object
del p1.age

# Whole object
del p1

# Empty class definition
class Person:
  pass




