#Python Collections(Arrays)
"""
    Therer are cour collection data types int he python programming language:

    List is collection which is ordered and changedable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members
    Set is a collection which is unordered, changeable and indexed. No duplicate members.

    When choosing a collection type, it is useful to understand the properties of that type. choosing the right type for a particular data set could mean retention of meaning, and it, 
    could mean an increase in effciency of security.


    Dictionary
"""

#List

thislist = ["apple", "banana", "cherry"]
print(thislist)

#Access Items
# you access the list items by referring to the index number:

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # banana

#Add Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

for x in thislist:
    print(x)

print("="*50)
thislist.insert(1,"watermelon")
for x in thislist:
    print(x)

print("="*50)
thislist.remove("apple")
print(thislist)

print("="*50)
thislist.pop(1)
print(thislist)

#The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# The del keyword can also delete the list completely:
del thislist
#print(thislist) # this will cause an error

#The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)