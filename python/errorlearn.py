# Error handling in python is similar to other languages with try except as the system

# The try block lets you test a block of code for errors
# The except block lets you handle the error
# The else block lets you execute code when there is no error
# The finally block lets you execute code regardless of results

try:
    print(x)
except:
    print("An exception occurred")

# Define many exception blocks for various error handling
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


# Example of else keyword. No issues raised so else block runs
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# The finally block runs regardless
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Close up resources where needed with finally
# demofile.txt does not exist so we get an exception raised.
# The error was trying to write to a file that does not exist, the exception was thrown as a result
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# Option to throw exceptions ourself
x = 5
if x < 0:
  raise Exception("Sorry, no numbers below zero")

# Raise typerror exception
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")