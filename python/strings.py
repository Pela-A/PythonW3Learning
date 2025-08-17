# Can use quotes opposite those surrounding the string

import sys


print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


# Multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings in Python are arrays of unicode characters.

# Get char at position
# Indexed starting at 0
a = "Hello, World!"
print(a[1])


# Loop through string (array of unicode characters)
for x in "banana":
  print(x)


# String length functions
a = "Hello, World!"
print(len(a))


# Comparison of two identical strings

b="Hello, World!"
c="Hello, World!"

# Check values of objects (sequence of characters)
print(b==c)

# Check if same object in memory (identity)
# Returns true because of "string interning"
# Python keeps a table of immutable strings 
print(b is c)


# String interning is when Python stores only one copy of an immutable string in memory. Later uses of the same string reuse the existing object instead of creating a new one.


#1 Short string between 0-20 characters are commonly interned
#2 Two identical string literals in the same Python file
#3 Strings that look like identifiers are more likely to be interned for performance.
#
#   Example "firstName" could be a valid variable string


# Runtime-generated strings are not interned automatically:


# Must import sys but we can manually intern strings
d = sys.intern("Some crazy complex string")



# In keyword with strings (can also you not)
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


# Strings are immutable in python
# c[1] = "c"

print(c)