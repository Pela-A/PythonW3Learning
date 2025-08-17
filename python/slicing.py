# Examine string slicing

# Start position is always included, end position not included


# Start position to index 5 not included
b = "Hello, World!"
print(b[:5])


# Position 2 to end
b = "Hello, World!"
print(b[2:])


# Negative indexing

# Basically just go backwards
# Should get orl
b = "Hello, World!"
print(b[-5:-2])
