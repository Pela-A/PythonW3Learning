# An iterator is an object that contains a countable number of values
# An iterable object is a container/object you can get an iterator from

# You can traverse through all the values

# Must implement __iter__() and __next__()

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple) # <class 'tuple_iterator'>
print(type(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# String iterable
mystr = "banana"
myit = iter(mystr) # <class 'str_ascii_iterator'>
print(type(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# For loops iterate through iterable objects
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)

# We can create an object/class as an iterator with the correct methods

class MyNumbers:
  
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)
print(type(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# StopIteration can be used to terminate/raise an error if iteration is done x number of times
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

# When looping through an iterable, it calls the next method on each pass
for x in myiter:
  print(x)
