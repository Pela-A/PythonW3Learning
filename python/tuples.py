# A tuple is one of 4 default/built in collection data types <class 'tuple'>
# Indexed collections can have duplicate values

# A tuple is indexed, ordered and unchangeable
# Unlike lists you use () to define a tuple.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuples are indexed and can be accessed using all list indexing rules from before (slicing reverse etc)
print(thistuple[0])

# Tuple length function
print(len(thistuple))

# Define a tuple of one item requires a , at the end
# TUPLE
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuples can be of any data type and contain different data types
tuple1 = ("abc", 34, True, 40, "male")

# The only way to change a value of a tuple is to convert to a list and then back to a tuple.
# Common strategy used even with strings

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# You cannot add individual items without either the same process or without adding a tuple to another

# Deleting an item in a tuple requires list workaround. You can delete an entire tuple with del keyword

#* Unpacking
# Similar to destructuring objects in JS.
# Like other iterables, we can unpack the object
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Can use an asterisk for assigning an unpacked value as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# Tuples are iterables, that are ordered and indexed and are immutable

# Identical to lists, since tuples are iterables
# Sequences are iterables that support indexing and order

# Tuples can be added together or multiplied by a number
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)