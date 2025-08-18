# Looking at logical conditions with if statement

a = 33
b = 200
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# You can create shorthand if and else statements
# AKA ternary operators or conditional expressions

# One line
if a > b: print("a is greater than b")

# Ternary
print("A") if a > b else print("B")

# Keywords are and or not

# Pass keyword for if statement with no actions
a = 33
b = 200

if b > a:
  pass

# pipe for or statement
if b | a:
  pass

# ampersand
if b & a:
  pass