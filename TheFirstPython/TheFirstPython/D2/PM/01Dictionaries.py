"""
Python Dictionaries

Dictionary
A dictionary is a collection which is unordered, changeable and indexed.
In Python dictionaries are written with curly brackets, and they have keys and values.
Associative array
"""

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(thisdict)

#way1 to get data
x = thisdict["model"]
print(x)

#way2 to get data
y = thisdict.get("model")
print(y)

#Change Values
#You can change the value of specific item by referring to its key name:

thisdict["year"] = 2018
print(thisdict)

print("*"*50)
#Loop through both keys and values, by using items() function:
for x,y in thisdict.items():
    print(x,y)

#Check if Key Exists

if 2018 in thisdict:
    print("ok")
else:
    print("no")


if "year" in thisdict:
    print("ok")
else:
    print("no")


if 2018 in thisdict.values():
    print("ok")
else:
    print("no")


# Adding Items
# Adding an item to the dictionary is done by
# using a new index key assigning a value to it:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = ""
print(thisdict)

#Removing items
#There are several methods to remove items from a dictionary

thisdict.pop("year")
print(thisdict)

#Remove the last inserted item
thisdict.popitem()
print(thisdict)

thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


del thisdict
#print(thisdict) #error because null


























