

"""
Phthon Lists
Python Collections (Arrays)
There are four collection data types in the Python programming language:

--List
    List is a collection which is ordered and changeable. Allows duplicate members.
--Tuple
    is a collectinon which is ordered and unchangeable allows 
--Set
    is a collection which is unordered and unindexed. No duplicate
--Dictionary 
    is a collectino which is unordered, changeable and indexed. No duplicate members.
"""

#List
# A list a collection which is ordered and changeable



weighttypes = ["Skinny", "Average", "Chubby","Fat"] 
print(weighttypes[0].casefold())

#Negative Indexing
print(weighttypes[-1].casefold())

#print(weighttypes[1:3].casefold())

print(weighttypes[:3])
print(weighttypes[:4])
print(weighttypes[:len(weighttypes)])
print("abc")
print(weighttypes[2:4])

#Range of Negative Indexes

#This example returns the items from index -4 (included) to index -1 (excluded)
print(weighttypes[-4:-2])

weighttypes[0] = "skinny"
print(weighttypes[2:4])
print("===================================================")
for x in weighttypes:
    print(x)

#Check if Item Exists

if "skinny" in weighttypes:
    print("Yes skinny is included")

    print(""" 
    q
     w   
        """)

# List Length

 #len() function:


 #Add Items
weighttypes.append("Super fat")
for x in weighttypes:
    print(x)

print("===========================================")
weighttypes.insert(0,"Super skinny")

for x in weighttypes:
    print(x)
print("===========================================")

weighttypes.remove("Super fat")
weighttypes.pop(0) #defalut the last index
for x in weighttypes:
    print(x)


print("===========================================")
del weighttypes[0]
for x in weighttypes:
    print(x)

print("===========================================")
weighttypes.clear()
for x in weighttypes:
    print(x)

#   프로그래밍 언어활용 NCS

import sys

num = "a\t       b\t"
num2 ="\tb"

print(sys.getsizeof(num))
print(sys.getsizeof(num2))



