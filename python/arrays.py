# Arrays are not built-in to python however lists are usable instead

# Define list and use list functions. Note that size limitations and type don't exist on lists. Use external library if need for array
cars = ["Ford", "Volvo", "BMW"]

# Index
x = cars[-2:-1]
print(x)

# Pop from list
lastCar = cars.pop()
print(lastCar)

# Append/add to list
cars.append("Toyota")

# Length
x = len(cars)

# Remove throws error if value not in list
# Only sets have the option to discard a value not in list and not throw error
cars.remove()