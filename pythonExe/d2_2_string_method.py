# 5. MODIFY STR
# Note: All string methods returns NEW values. They do not change the original string.

b = "Bonjour Vietnam"
# str.UPPER() - returns the string in upper case
print(b.upper())  # BONJOUR VIETNAM

# str.LOWER()
print(b.lower())  # bonjour vietnam

# string.strip(characters-optional) - remove white space
c = "    Bonjour Vietnam!  "
print(c.strip())  # Bonjour VietFnam!
txt_st = ",,,,,rrttgg.....banana....rrr"
st = txt_st.strip(",.grt")
print(st)  # banana

# str.REPLACE(oldvalue, newvalue, count) - replace a str with another str
# Note: All occurrences of the specified phrase will be replaced, if nothing else is specified.
print(b.replace("V", "Z"))  # Bonjour Zietnam

txtrep = "one one was a race horse, two two was one too."
rep1 = txtrep.replace(
    "one", "THREE"
)  # THREE THREE was a race horse, two two was THREE too.
rep2 = txtrep.replace(
    "one", "THREE", 2
)  # THREE THREE was a race horse, two two was one too.
print(rep1)
print(rep2)

# string.SPLIT(separator-optional, maxsplit- optional) - splits the string into substrings
d = "Xin chao, Vietnam"
print(d.split(","))  # ['Xin chao', ' Vietnam']

txt_sp = "apple#banana#cherry#orange"
sp1 = txt_sp.split("#")
print(sp1)  # ['apple', 'banana', 'cherry', 'orange']
# setting the maxsplit parameter to 1, will return a list with 2 elements!
sp2 = txt_sp.split("#", 1)
print(sp2)  # ['apple', 'banana#cherry#orange']

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

# string.INDEX(value, start, end) - find the first occurrence of the specified value
txt_in = "Hello, welcome to my world."
x_in1 = txt_in.index("e")
print(x_in1)  # 1
x_in2 = txt_in.index("e", 5, 10)
print(x_in2)  # 8

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

# string.ISALPHA() - returns True if all the characters are alphabet letters (a-z)
txt_isal1 = "CompanyX"
txt_isal2 = "Company10"
print(txt_isal1.isalpha())  # True
print(txt_isal2.isalpha())  # False

# string.ISNUMERIC() - returns True if all the characters are numeric (0-9), otherwise False
# Exponents, like ² and ¾ = numeric values.
# "-1" and "1.5" are NOT considered numeric values,
# because all the characters in the string must be numeric, and the - and the . are not.
a = "\u0030"  # unicode for 0
b = "\u00B2"  # unicode for ²
c = "10km2"
d = "-1"
e = "1.5"
f = "12345"

print(a.isnumeric())  # True
print(b.isnumeric())  # True
print(c.isnumeric())  # False
print(d.isnumeric())  # False
print(e.isnumeric())  # False
print(f.isnumeric())  # True

# string.ISALNUM() - returns True if all the characters are alphanumeric - (a-z) and (0-9)
txt_isan1 = "Vietnam84"
txt_isan2 = "Vietnam 84"
print(txt_isan1.isalnum())  # True
print(txt_isan2.isalnum())  # False

# string.JOIN(iterable) - takes all items in an iterable and joins them into one str
myTuple = ("John", "Peter", "Vicky")
mtj = "#".join(myTuple)
print(mtj)  # John#Peter#Vicky
# Note: When using a dictionary as an iterable, the returned values are the keys, not the values.
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
mdj = mySeparator.join(myDict)
print(mdj)  # nameTESTcountry

# string.title() - returns a string where the first character in every word is upper case
# if number+Str --> the first letter after that will be converted to upper case.
txt_tt = "Welcome to my 2nd world"
tt = txt_tt.title()
print(tt)  # Welcome To My 2Nd World
# the first letter after a non-alphabet letter is converted into a upper case letter
txt_tt1 = "hello b2b2b2 and 3g3g3g"
tt1 = txt_tt1.title()
print(tt1)  # Hello B2B2B2 And 3G3G3G
