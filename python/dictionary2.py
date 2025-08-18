# A dictionary is one of the 4 collection data types provided by python by default

# use a for loop to loop through a dictionary

# Default it returns the keys of dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x)
  # Grab keys value
  print(thisdict[x])

# Use values() method to return values of dict
for x in thisdict.values():
  print(x)

# Or use keys() method to return keys of dict
for x in thisdict.keys():
  print(x)

# Option 3 is to use items() method to reutnr both key and values
for x, y in thisdict.items():
  print(x, y)


# Similar to all other data types, you need to use copy() method or constructor dict() method to create a copy
# Otherwise you get a reference
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict1 = thisdict
mydict2 = thisdict.copy()
# True because this will be a reference
print(mydict1 is thisdict)
# False because we created a copy
print(mydict2 is thisdict)

#* NESTED DICTIONARIES
# We are allowed to nest dictionaries inside dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Accessing nested level involves first grabbing the nested dictionary we want to look at then looking at the key value pair
print(myfamily["child2"]["name"])

for key, value in myfamily.items():
  print(key, value, sep=": ")

  for y, z in value.items():
    print(y,z, sep=": ")


# BONUS METHODS
# setdefault method to specify a default value if a value is not present
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.setdefault("color", "red")
print(car)

# fromkeys method takes an iterable x and default value y to create a dictionary with keys being the iterables and values being the default
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)


# Examining what can and can't be a key
# Keys must be hashable
# This means that it has a __hash__() method and its value does not change over its lifetime or is immutable
# int, float, str, tuple (if all elements are hashable), and a "frozenset" (an immutable set)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  100: 2000,
  True: False,
  (1,2,3): "Tuple!",
}

print(car[100])
print(car[True])
print(car[(1,2,3)])
