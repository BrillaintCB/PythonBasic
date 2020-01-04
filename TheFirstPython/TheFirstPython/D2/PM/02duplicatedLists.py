a = [1,2,3,['a','b','c'],4,5]
 
print(a[2:5]) #3,['a','b','c'],4


b = (1,2,3)

c = list(b)

c.append(4)

b = tuple(c)

print(b)

d = b + (5,)
print(d)


b = b + (5,)
print(b)