
"""
    Strings are Arrays
    Like many other popular programming languages, strings in Python are arrays of bytes
    representing unicode characters

    However, Python does not have a charater data type, a single charater is simply a string with 
    a length of 1.

"""

a = "Hello World!"
print("H expected",a[0]) # H


"""
    Slicing
    You can return a range of charaters by using the slice syntax.
    Specify ther start index and the end index, separated by a colon, to return a part of the string.
"""

b = "Jhonie walker"
print("Jhonie expcted",b[0:5+1]) #Jhonie
print("Jhonie walker expcted",b[0:19]) #Jhonie walker

# Nagative indexsing 
# Get the charaters from 6 to positing 2(excluding), starting the count from the end of the string:
# a[0:3] means 0 <= a < 3

print(b[-6:-2]) #walk
print(b[2:5]) #oni
print(b[0:3]) #Jho
print(b[-1]) #r
print(b[-2]) #e
print(b[-2:-1]) #e
print(b[-3:-1]) #ke


print("*"*50)
a = "20200104Sunny"
date = a[4:8]
date = a[:8]
weather = a[8:]
print(date)
print(weather)

# immutable 

a = "Pithon"
a[1] = "y" # this will cause an error because string is 
           # immutable data type
print(a[1])




b = "Python"
length = len(b)
print("6 expected",length) #6


b = " Python  "
length = len(b)
print("9 expected",length)
#strip() removes any whitespace from the beginning or the end:

length = len(b.strip())
print(length) #6

#lower() returns the string in lower case:

print(b.lower())
print(b.upper())
# replace() method replaces a string with another string:
print(b.replace("o", "OOO"))

#split() method splits the string into substrings if it finds instances of the separator:

a = "Paul: Reece: Emliy"

print(a.split(":")) 

c = a.split(":")
print(c[0]) #paul

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