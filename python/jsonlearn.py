# json module can be used to work with json in python
# JavaScript Object Notation
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

# json.dumps() method to convert python objects into JSON
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# conversions
# Python	JSON
# dict	    Object
# list	    Array
# tuple	    Array
# str	    String
# int	    Number
# float	    Number
# True	    true
# False	    false
# None	    null


import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

print(json.dumps(x, indent=4))

# Separator tuple first parameter changes commas that separate items in a JSON
# Second parameter changes the colons that separate keys and values
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Finally we can also sort the keys
print(type(json.dumps(x, indent=4, sort_keys=True)))
print(json.dumps(x, indent=4, sort_keys=True))