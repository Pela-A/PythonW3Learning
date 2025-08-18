# A set is one of the 4 collection data types provided by python by default <class 'set'>

# Sets have the following rules
# They are iterables
# Are not ordered (not a sequence)
# Unchangeable
# Duplicate values are not allowed (they will be ignored)

# Sets are define with curly braces and no key value pairings
thisset = {"apple", "banana", "cherry"}
print(thisset)
print(type(thisset))

# True and 1 are the same value as is False and 0
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# A python set IS considered an iterable and therefore can be looped through
# NOTE an iterable is considered any object that contains the __iter__() method that returns some iterator or __getitem__() with integer indices starting at 0

# Sets can be of any data type and contain different data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set1 = {"abc", 34, True, 40, "male"}

# Like lists and tuples, we can use the constructor for the class type
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


#* Accesing Sets
# Sets can not be accesed through indexes or keys so you have to either loop through or check if a specific value is in the set.
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
# Use not in for checking if not in (true if not in false if in)


#*Adding and removing set items
# add method for adding individual items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# update method for adding items from an iterable to a set
# Set iterable on set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# List iterable on set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# Removing items in a set requires the remove or discard method

# Remove method will raise an error if item to remove does not exist
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

# Discard method will not raise an error if item to remove does not exist
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# Pop method is random for sets
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# Clear method to empty a set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# del keyword to delete the set completley
thisset = {"apple", "banana", "cherry"}
del thisset

# Loop through sets with for loops
# This will be random since it is unordered
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#* Joining sets
# Union method will return a new set with items from both sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# Using the pipe operator instead of union method acheives the same result
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

# Can add multiple sets in union method and with pipe operator
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

# Pipe operator multiple
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

# union method can be used with any iterable
# Take a set, call union method with iterables

# pipe operator tech can only be used with sets

# Update method is another way to merge sets. Note that a new set is not created.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2,set3)
print(set1)

# Intersection method creates a new set. It only keeps duplicates between the sets. There is an option for using ampersand however it follows the same rule as before. Iterables can be used for intersection but not for ampersand
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# ampersand method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

# intersection_update() method keeps duplicates but will change original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

# Difference method returns a new set containing items in set1 that are not in set2 only
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

# Like with other methods you can use a different operator - but can only use sets instead of any iterable
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

# difference_update to change original set instead
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

# symmetric_difference() method will keep elements not present in both sets, creating a new set
# Everything but apple
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

# using the carrot operator we can get the same result but only use sets instead of also iterables
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

# Like with other methods, adding _update will remove duplicates between two sets but just change the original set instead
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

# BONUS adding = to the shortcut operators will use the update method (update the existing set instead)

# There are also subset methods (set is fully a part of another) (it is a part of another)

# And a superset method (the set contains all items from another set) (contains a part of another )