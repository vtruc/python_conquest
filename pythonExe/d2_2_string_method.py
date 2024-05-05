# 5. MODIFY STR
# Note: All string methods returns NEW values. They do not change the original string.

b = "Bonjour Vietnam"
# str.UPPER() - returns the string in upper case
print(b.upper())  # BONJOUR VIETNAM

# str.LOWER()
print(b.lower())  # bonjour vietnam

# str.STRIP() - remove white space
c = "    Bonjour Vietnam!  "
print(c.strip())  # Bonjour VietFnam!

# str.REPLACE() - replace a str with another str
print(b.replace("V", "Z"))  # Bonjour Zietnam

# str.SPLIT() - splits the string into substrings
d = "Xin chao, Vietnam"
print(d.split(","))  # ['Xin chao', ' Vietnam']

# more str methods
# str.CAPITALIZE() - 1st char in 1st word of the sentence is upper case (the rest is lower case)
text1 = "hello and welcome to Vietnam"
x = text1.capitalize()
print(x)  # Hello and welcome to vietnam
text2 = "welcome to VIETNAM"
y = text2.capitalize()
print(y)  # Welcome to vietnam
text3 = "84 is my id"
z = text3.capitalize()
print(z)  # 84 is my id

# str.COUNT(value, start, end)
text4 = "I love apples, apple are my favorite fruit"
t41 = text4.count("apple")
t42 = text4.count("apple", 10, 24)
print(t41)  # 2
print(t42)  # 1

# str.FIND(value, start, end)
# finds the first occurrence of the specified value, NOT FOUND --> -1
txt1 = "Hello, welcome to my world."
x1 = txt1.find("welcome")
print(x1)  # 7
x2 = txt1.find("e")
print(x2)  # 1
x3 = txt1.find("e", 5, 10)
print(x3)  # 8
# NOT FOUND - find() returns -1, index() raises exception "ValueError: substring not found"
print(txt1.find("q"))  # -1
# print(txt1.index("q"))  # ValueError: substring not found

# str.FORMAT(value1, value2...)
# formats the specified value(s) and insert them inside the string's placeholder {}.
# returns the formatted string
# PLACEHOLDERS:
# (1) name indexes
txt21 = "My name is {fname}, I'm {age}".format(fname="Tristine", age=85)
# (2) numbered indexes
txt22 = "My name is {0}, I'm {1}".format("Tristine", 85)
# (3) empty
txt23 = "My name is {}, I'm {}".format("Tristine", 85)
print(txt21)  # My name is Tristine, I'm 85
print(txt22)  # My name is Tristine, I'm 85
print(txt23)  # My name is Tristine, I'm 85
# formating types inside placeholder
# :,
txt3 = "The current population of Vietnam is {:,}.".format(90000000)
print(txt3)  # The current population of Vietnam is 90,000,000.
# :%
txt4 = "The interest rate for 6 months is {:%}."
print(txt4.format(0.046))  # The interest rate for 6 months is 4.600000%.
txt5 = "The interest rate for 6 months is {:.0%}."
print(txt5.format(0.046))  # The interest rate fFor 6 months is 5%.
print(txt5.format(0.045))  # The interest rate for 6 months is 4%.