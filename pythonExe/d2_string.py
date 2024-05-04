# 1. STRINGS ARE ARRAYS
# strings in Python are arrays of bytes representing unicode characters.
# Python does not have a character data type, a single character = a string with len = 1.
# Square brackets can be used to access elements of the string.
a = "I love Vietnam"
print(a[5])  # e

# 2. STRING LENGTH
print(len(a))  # 14

# 3.CHECK STRING - To check if a certain phrase or character is present in a string
# a. IN
print("Vietnam" in a)  # True
# if statement
if "Vietnam" in a:
    print('"Vietnam" is present.')  # "Vietnam" is present.

# b. NOT IN
print("Vietnam" not in a)  # False
# if statement
if "apple" not in a:
    print('"apple" is not present.')  # "apple" is not present.

# 4. SLICING STRINGS - str[start index : end index (not included)]
b = "Bonjour Vietnam"
print(b[2:5])  # njo
# Note: The first character has index 0.
print(b[:5])  # Bonjo
print(b[2:])  # njour Vietnam
print(b[-5:-2])  # etn

# 5. MODIFY STR
# str.upper() - returns the string in upper case
print(b.upper())  # BONJOUR VIETNAM
# str.lower()
print(b.lower())  # bonjour vietnam
# str.strip() - remove white space
c = "    Bonjour Vietnam!  "
print(c.strip())  # Bonjour Vietnam!
# str.replace() - replace a str with another str
print(b.replace("V", "Z"))  # Bonjour Zietnam
# str.split() - splits the string into substrings
d = "Xin chao, Vietnam"
print(d.split(","))  # ['Xin chao', ' Vietnam']

# more str methods
# str.capitalize() - 1st char in 1st word of the sentence is upper case (the rest is lower case)
text1 = "hello and welcome to Vietnam"
x = text1.capitalize()
print(x)  # Hello and welcome to vietnam
text2 = "welcome to VIETNAM"
y = text2.capitalize()
print(y)  # Welcome to vietnam
text3 = "84 is my id"
z = text3.capitalize()
print(z)  # 84 is my id
