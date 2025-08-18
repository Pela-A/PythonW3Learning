# A for loop is one of two primitive loop commands
# It is used to iterate over an iterable not just over a sequence

# Can use break or continue statements if wanted

# Can use range types to loop a certain number of times
x = range(6)
print(type(x))

for x in range(6):
    print(x)

# Specify starting position
for x in range(2,6):
    print(x)

# Change default increment with third parameter
for x in range(2,30,3):
    print(x)

# Can add an else block after for loop like with while however break statements prevent block from being executed

# Nest loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  # Loop through fruits occurs for each iteration of adj list iterable
  for y in fruits:
    print(x, y)
# Pass statement to have an empty for loop.

for x in [0, 1, 2]:
  pass
