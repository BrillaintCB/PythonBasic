
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