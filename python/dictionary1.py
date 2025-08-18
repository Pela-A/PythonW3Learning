# Dictionaries are one of the 4 collection data types provided by python by default <class 'dict'>

# They are used to store key value pairs
# They have the following rules
# A dictionary is 'ordered'
# Changeable
# Duplicates are not allowed

# Dictionaries are not considered a sequence (likely because it is not indexed in order but uses keys?)
from collections.abc import Sequence

testdict = {"h":1}
print(type(testdict))
print(isinstance(testdict, Sequence))  # False (dictionary is not a sequence)


# Example dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# What value is taken when writing duplicate keys?
# The last written one
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# len() function

#* Accesing
# Access using square brackets and key or using get() method on dictionary with key
x = thisdict.get("model")

# Get list of keys in dictionary <class 'dict_keys'>
x = thisdict.keys()
print(type(x))

# keys() list updates even if you add a new key after grabbing key list
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

# Grab values in the dictionary <class 'dict_values'>
x = thisdict.values()
print(type(x))

# Same behavior occurs if we change a value

# items() method returns each item in list as a tuple <class 'dict_items'>
x = thisdict.items()
print(type(x))

# Same dynamic behavior
# Can use in to check if a key is present on a dictionary

# Can use update method with iterable objects that contain key:value pairs (for now that is just dictionaries?)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# Add items with update method or using a new key and assigning a value

#* Removing items
# pop() method removes specified item with key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# popitem() method removes the last inserted item 3.7 and after
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# del keyword to remove hte item with key name or can delete whole dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
del thisdict

# clear() method to empty the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)