#* Sorting
# Python will sort lists alphanumerically
# Sorts by unicode values not ascii
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# This works for numbers. 

# Note you can not mix data types for list sort method
# One solution is to cast as string
testlist = ["orange", 100]
testlist.sort(key=str)

# Sort descending instead of ascending (default)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


# You can customize the sort function to modify values in list before sorting
def myFunc(n):
    return abs(n-50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myFunc)
print(thislist)


# Final option is to just reverse the list. No sorting.
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.reverse()
print(thislist)


#* List copying
# When trying to copy lists, python by default will only give you a reference to that list. 

newlist1 = ["apple", "banana", "cherry"]
newlist2 = newlist1
print(newlist1 is newlist2)

# We need to use a method/constructor to create a unique copy
newlist1 = ["apple", "banana", "cherry"]
# Copy
newlist2 = newlist1.copy()
# List constructor/method
newlist3 = list(newlist1)
# Slice
newlist4 = newlist1[:]

print(newlist1 is newlist2)
print(newlist1 is newlist3)
print(newlist1 is newlist4)


#* Joining lists
# Adding
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Looping
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Extend method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

