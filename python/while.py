# While loops are one of two primitive loop commands in python
# Execute statements while condition is true
i = 1
while i < 6:
    print(i)
    i += 1

# break statement can stop a loop even if the condition is still true

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i+=1

# The continue statement can move on to the next iteration
i = 0
while(i<6):
    i+=1
    if(i==3):
        continue
    print(i)

# We can run a block of code with else statement after the while condition is no longer true
i = 1
while i < 6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")

# What if we break out of the while loop will the if statement run?
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i+=1
else:
    print("Else statement reached!")
# No it will not