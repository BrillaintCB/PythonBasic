
"""
Difference between Find and Index
"""

str = "Hello World"

#Common Both return index if there is found data
a = str.find("o")
a = str.index("o")

#Difference 
a = str.find("y")
print(a)  # find() return -1 if there is no found data

#index() will cause an error if there no found data
#a = str.index("y")
#print(a)





