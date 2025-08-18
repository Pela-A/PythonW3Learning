# Avoid name conflicts don't use math.py

# Built in functions include min max functions, absolute value and pow
# Min max functions
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

# Absolute value
x = abs(-7.25)
print(x)

# Power function
x = pow(4, 3)
print(x)


# Math module contains useful math functions
import math
x = math.sqrt(64)
print(x)

# Ceiling rounds up, floor down
import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1

# pi constant
import math
x = math.pi
print(x)

# Math module reference for more information in future