# In python we can get user input
print("Enter your name:")
name = input()
print(f"Hello {name}")

# Use prompt parameter inside input function to put message in front of user input on same line
name = input("Enter your name: ")
print(f"Hello {name}")

# python stops executing code at each input until user input is accepted

# Input from user is treated as a string by default
import math
x = input("Enter a number:")

# find the square root of the number:
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")

# Validate input using while loop with try except
y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")
