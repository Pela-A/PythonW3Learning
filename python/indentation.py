# A tab is typically 4 spaces but this can be editor dependent. PEP 8 convention is 4 spaces

#PEP 8, or Python Enhancement Proposal 8, is the official style guide for Python code.

# Define variable if 0 show valid spacing else show invalid
x = 0

# Note you don't need parathenses for if statements however it's just better in my opinion for readability and more complex boolean conditions
if x == 0:
 print("Indentation has to be at least one space however")
 print("indentation must match")
elif x == 100:
   pass
else:
    print("This will fail?")
    # Add indentation to prove failure
    print("bad")
  
# Empty code blocks can not exist
  

# Indentation does not need to match in different if statements, a single if statement must have matching indentation

# Will explore errors further but it seems that syntax errors will be caught by python compiling into byte code however runtime errors won't be caught ever.



