"""
Set 
A set is colelctino which is unordered and unindexed
In python sets are written curly brackets
"""

thisset = {"apple","banana","cherry"}

for x in thisset:
    print(x)

print("banana" in thisset);

#Change Items 
#Once a set is created, you can not change its items,
#but you can add new items

thisset.add("orange")
#for x in thisset:
#    print(x)
print(thisset)

#To add more than once item to a set use the update()

thisset.update(["mango", "grapes"])
print(thisset)

#Remove Item
# To remove an item in a set, use the remove()
# or the discard() method.

thisset.remove("mango")
print("*"*50)
print(thisset)
thisset.remove("orange")
print("*"*50)
print(thisset)

#you can use pop() method: to remove the last item
#cherry is going to be removed

thisset.pop()
print(thisset)

thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}

#del thisset   #delete the set completely

#print(thisset)

#The union() method returns a new set with all items from both sets

set1 = {"a","b","c"}
set2 = {1,2,3}

#way1
set3 = set1.union(set2)
print(set3)

#way2
set1.update(set2)
print(set1)
















