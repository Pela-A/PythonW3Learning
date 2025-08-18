# Lists are basically an array list equivalency in python

# Indexed, ordered, mutable


# Array length function
thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# Lists can contain different data types
list1 = ["abc", 34, True, 40, "male"]

# Type of list = <class 'list'>

#* INDEXING
# Similar to string indexing. Allows for normal indexing, negative, slicing/ranges

#* CHANGE
# Can change individual indexes of a list or a range
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


# Insert function allows us to add items to the list at any index. Values at and after index will be pushed to the right 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Append function adds item to end of list. Useful for stack like implementations
# Last in, First out
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# The extend method allows us to append/add any iterable object (indexed/have an iterator aka an object with a __next__() method)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# For dictionaries it only appends the key but also I really don't see a point you might use this
thislist = ["apple", "banana", "cherry"]
thisDict = {"kiwi2": "orange2"}
thislist.extend(thisDict)
print(thislist)


#* Removing
# remove() method removes first occurence of a specified value
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# pop() method removes the last item of list by default or can be specified for a certain index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# del keyword can let us delete specific indexes or entire lists
# Index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Whole list
thislist = ["apple", "banana", "cherry"]
del thislist

# Finally we can empty a list. Meaning we have a list with no entries.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)