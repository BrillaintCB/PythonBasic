
#int
x = 5
print(x, type(x))

# float
x = 20.5
print(x, type(x))
#complex
x = 1j
print(x, type(x))

#str
x = "James"
print(x, type(x))

#list

x = ["apple", "banana","tomato"]
print(x, type(x))

#tuple
x = ("apple", "banana", "tomato")
print(x, type(x))

#range (range 0,3)
x= range(3)
print(x, type(x))

#dict
x = {"name" : "James", "id": 1}
print(x, type(x))

#set
x = {"apple", "banana", "tomato"}
print(x, type(x))

#frozenset
x = frozenset({"apple", "banana", "tomato"})
print(x, type(x))

#bool
x = True
x = False;
print(x, type(x))

#bytes
x = b"Hello"
print(x, type(x))

#bytearry
x = bytearray(5)
print(x, type(x))

#memoryview(byte(5))
x = memoryview(bytes(5))
print(x, type(x))


#Setting the Specific Data Type
#Type Conversion
x = 1
x = str(x)
x = int(x)
x = float(x)
x = complex(x)
x = bool(x)
print(x, type(x))


"""
This is multi line comments
"""
#Python Numbers

#convert from int to float:
a = float(x)

#convert from float to int:

#Random Number

import random
print(random.randrange(1,20))

"""
String Literals
    string literls in python are surrounded by either
    single quotation marks, or double quotation marks.
    'hello' is the same as "hello"
"""

#Multiline Strings
"""
    
"""

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)





#Boolean Values

print('single'=="single")
print(int(5.5)==5)
print(float(5)==int(5))
print("5"==int(5))

a = int(200)
b = float(55.5)

if b>a:
    print("b>a")
else:
    print("b<a")

"""
Some Values are False
In fact, there are not many values 
that evaluates to False, 
except empty values, 
such as (), [], {}, "", 
the number 0, and the value None.
And of course the value False evaluates to False.
"""


mylist = ["apple", "bannaa", "orange"]
x = len(mylist)
print(bool(x))

print(bool("abc"))

print(bool(0))


"""
    Python Identity Operators
    
"""
if(int(5) is float(5)):
    print("int 5 is equal to float 5")
else:
    print("Not eqaul")


"""
    Strings are Arrays
    Like many other popular programming languages, strings in Python are arrays of bytes
    representing unicode characters

    However, Python does not have a charater data type, a single charater is simply a string with 
    a length of 1.

"""

a = "Hello World!"
print(a[0])


"""
    Slicing
    You can return a range of charaters by using the slice syntax.
    Specify ther start index and the end index, separated by a colon, to return a part of the string.


"""

b = "abcdefg"
print(b[0:19])


# Nagative indexsing 
# Get the charaters from 5 to positing 1, starting the count from the end of the string:
print(b[-5:-2])
print(b[2:5])
print(b[0:3])
print(b[-1])

b = "Python"

length = len(b)
print(length)

#strip() removes any whitespace from the beginning or the end:

b = " Python  "
length = len(b)
print(length)

length = len(b.strip())
print(length)

#lower() returns the string in lower case:

print(b.lower())
print(b.upper())
# replace() method replaces a string with another string:
print(b.replace("o", "OOO"))

#split() method splits the string into substrings if it finds instances of the separator:

a = "Paul: Reece: Emliy"

print(a.split(":"))

#capitalize()
a = "capitalize"

print(a.capitalize())

#casefold() 
"""
casefold()  is similar to the lower() method,
but the casefold() method is stronger,
more aggressive, meaning that it will convert 
more characters into lower case, 
and will find more matches when comparing two strings and
both are converted using the casefold() method.
"""

a = "banana"
acenter = a.center(10)
print(acenter)


#check String
# To check if a certain phrase or character is present in a string, we can use the ekywords in or not in


txt = "Show me the money"
x = "the" in txt
print(x)

txt = "Show me the money"
x = "the" not in txt
print(x)

#String Concatenation

a = "Show me"
b = "the money"
c = a + b
print(c)

# String Format  --format()
date = 28
txt = "Today is {}"
print(txt.format(date))

qty = 3
itemno = 567
price = 50.45
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(qty, itemno, price))


price = 50.45
qty = 3
itemno = 567
myorder = "I want {2} pieces of item {1} for {0} dollars."
print(myorder.format(price,itemno,qty))


#Escape Character
# Backspace
abcd = "Hello \bWorld"
abcd = "Hello\tWorld"
print (abcd)

