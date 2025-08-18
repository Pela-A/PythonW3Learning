# Explore different ways to loop through lists

# Use for blank in list[]
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# Loop through each index in a range specified by length of list
thislist = ["apple", "banana", "cherry"]
# Range creates an iterable "range object" starting at zero, incrementing by 1 and ending and excluding the end value
for i in range(len(thislist)):
  print(thislist[i])


# While loops are another option
thislist = ["apple", "banana", "cherry"]
i = 0
while(i < len(thislist)):
  print(thislist[i])
  # Increment index for each iteration
  i = i + 1


# Final option is list comprehension. Will not go too into depth here as there is a whole chapter on it coming up but it seems like you create a loop condition and response on one line.
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


#* List comprehension
# W3 Schools leaves this explanation
# newlist = [expression for item in iterable if condition == True]

# You have an expression you want as a result, your looped list, followed by a condition that determines whether or not the expression is evaluated
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


# Condition is a filter that is optional
# list is actually an iterable so we could use any iterable object
newlist = [x for x in range(10)]

# Expression is considered both the current item in the iteration and the outcome.
newlist = [x.upper() for x in fruits]

# We can also manipulate the outcome expression with a condition inside the expression
newlist = [x if x!= "banana" else "orange" for x in fruits]
# returns item in iteration if not banana. If it says banana we return orange





