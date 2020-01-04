"""
Tuple 

A tuple is a collection which is ordered and unchangeable. In Python tuples
are written with round brackets
"""

thistuple = ("apple","banana", "orange")
print(thistuple)

#Access Tuple Item

thistuple = ("apple","banana", "orange")
print(thistuple[1]) #banana


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[2:4]) #cherry , orange


#Change Tuple Values
"""
Once a tuple is created, you cannot change its values. Tuples 
are unchangeable, or immutable as it also called.

But there is a workaround. You can convert the tuple into a list, change
the list, and convert list back into a tuple
"""


x = ("apple","banana", "orange")
y = list(x)
y[1] = "kiwi"

x= tuple(y)

#Loop Through a Tuple
for x in y:
    print(x)

# Check if Item Exists
print("*"*50)
print(x)
print("*"*50)

if "apple" in x:
    print("There is an apple")
else:
    print("Not found")


x = ("apple","banana", "orange")
if "apple" in x:
    print("There is an apple")
else:
    print("Not found")

# Create Tuple With One Item

thistuple = ("apple",)
print(type(thistuple))

#Not a tuple
thistuple = ("apple")
print(type(thistuple)) #String


# del keyword
thistuple = ("apple", "banana", "cherry")
#del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

#Join Two Tuples

tuple1 = ("a","b","c")
tuple2 = (1,2,3,1)
tuple3 = tuple1 + tuple2
print(tuple3)


idx = tuple3.index("c")
print(idx)

cnt = tuple3.count(1)
print(cnt)














