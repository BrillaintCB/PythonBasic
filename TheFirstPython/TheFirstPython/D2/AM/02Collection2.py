
"""
Copy a List

you cannot copy a list simply by typing list2 = list1 , because: lists2 will only be a reference to list1,
and changes made in list1 will automatically also be made in list2
"""

# way 1
thislist = ["apple", "banana", "cherry"]
copylist = thislist.copy()
print(copylist)

# way 2
thislist = ["apple", "banana", "cherry"]
copylist = list(thislist)
print(copylist)

#Join Two Lists
"""
There are several ways to join, or concatenate, two ro more lists in Python.
"""
# way 1  using the + operator

list1 = ["a", "b", "c"];
list2 = [1, 2, 3];

list3 = list1 + list2
print(list3)


#Multiplication 
print(list3 * 2 )

for x in list3:
    print(type(x))



#Way 2 for append

list1 = ["a", "b", "c"];
list2 = [1, 2, 3];

for x in list2:
    list1.append(x)

print("*"*50)
print(list1)
print("*"*50)

#way 3 extend

list1 = ["a", "b", "c"];
list2 = [1, 2, 3];

list1.extend(list2)
print(list1)


print("*"*50)

#The list() Constructor
# It is also possible to use the list() constructor to make a new list.



















#Octal 8
a = 0o177
print(a)

#Hex 16
b = 0xABC
print(b)


a = 14
b = 3

c = 14%3
d = 14//3

print(c)
print(d)








