# Inheritance allows us to have a parent class, and a child class which derives from the parent class

# Start with our parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()

# Inherit by placing inherited class inside parantheses
class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

# Here we can either overwrite functions from parent class or add new ones
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

# Super function can be used for child class to inherit all the methods and properties from parent
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

# Add a new method to child class
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
