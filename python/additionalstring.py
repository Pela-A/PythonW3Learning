# Escape Characters

# An escape character is a backslash \ followed by the character you want to insert.

txt = "We are the so-called \"Vikings\" from the north."

print(txt)




# \'	Single Quote
# \"	Double Quote
# \\	Backslash
# \n	New Line


# \r	Carriage Return
# Return to start of line and start overwriting.

txt = "Hello\rWorld!"
print(txt) 
print("Hello World\rPython")

# Example creating a progress bar/real time update
# import time

# for i in range(11):
#     print(f"\rProgress: {i*10}%", end="")
#     time.sleep(0.5)
# print("\nDone!") # Add a newline at the end

# \t	Tab
# \b	Backspace

# Remove previous character?????

print("Hello\bWorld")

# Example from reddit
# from time import sleep

# s="|/-\\"

# print("Loading....", end="", flush=True)

# for i in range(20):
#     print(f"\b{s[i%len(s)]}", end="", flush=True)
#     sleep(0.5)


# \f	Form Feed (text formatting when writing to a file, tells to go to a new page)


# \ooo	Octal value
# Represent octal code of ASCII

# \xhh	Hex value
# Represent hex codes of ASCII


# Ton of string methods here
# https://www.w3schools.com/python/python_strings_methods.asp


# Capitalize first character
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)


# casefold is safer for internationalized text (uses works with unicode rather than ASCII)
a = "Straße"
b = "strasse"

# Using lower()
print(a.lower() == b.lower())      # False

# Using casefold()
print(a.casefold() == b.casefold()) # True


# Center method aligns a string in middle
# takes optional second parameter to determine what fills empty space on both sides
txt = "banana"

x = txt.center(20, "*")

print(x)


# count() return number of times a value occurs in a string
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)


# Encode
txt = "My name is Ståle"

x = txt.encode()

print(x)


# endswith method return boolean if string ends with specified value
txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)


# expandtabs to edit tab spacing
# escape character tabs default in python are 8 spaces
txt = "H\te\tl\tl\to"

x =  txt.expandtabs(4)

print(x)


# Find method finds the first occurrence of specified value
txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)


# format method to place specified values inside string placeholder
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)


# index is similar to find but raises an exception instead of -1 if value not found
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)


# isalnum checks if all characters are alpha numeric (a-z), (0-9)
# Useful for some leetcode questions
txt = "Company12"

x = txt.isalnum()

print(x)


# check if all characters are letters
txt = "CompanyX"

x = txt.isalpha()

print(x)


# check if all characters in the text are ascii characters
txt = "Company123"

x = txt.isascii()

print(x)


# Check if all characters are decimals (unicode aware)
txt = "1234"

x = txt.isdecimal()

print(x)


# Expands on isdecimal() Checks if all characters are digits (includes exponents, sub, and superscripts) (unicode aware)


# The isidentifier() method returns True if the string is a valid identifier, otherwise False.

# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces
txt = "Demo"

x = txt.isidentifier()

print(x)


# Is numeric is super broad contains more valid characters than isdigit method
# Chinese numeral
print("四".isdecimal(), "四".isdigit(), "四".isnumeric())


# isprintable returns true if all characters are printable (no escape characters ex.)
txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)


# Check if all characters are whitespace
txt = "   "

x = txt.isspace()

print(x)


# The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False. title() to convert a string to a proper title format

txt = "22 Hello, And Welcome To My World!"

x = txt.istitle()

print(x)


# The ljust() method will left align the string, using an optional specified character (space is default) as the fill character. rjust() for right adjust
txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")

# rfind() last position value found. rindex exists as well but will raise an exception if not found

# swapcase() swaps letter casings