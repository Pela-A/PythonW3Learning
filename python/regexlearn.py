# Python has a regex module for working with regular expressions
# Regular expressions are a sequence of characters that forms a search pattern
import re
txt = "The rain in spain"
x = re.search("^The.*spain$", txt)

print(x)

# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

# We are not studying all regex rules in this project that is like an entire separate project