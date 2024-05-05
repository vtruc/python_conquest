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