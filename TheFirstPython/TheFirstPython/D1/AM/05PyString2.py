
#check String
# To check if a certain phrase or character is present in a string, we can use the ekywords in or not in


txt = "Show me the money"
x = "the" in txt
print(x) #True

txt = "Show me the money"
x = "the" not in txt
print(x) #False

example1 = "Jim beam"
result1 = "Jim" in example1
print("True", result1) #true

#String Concatenation

a = "Show me"
b = "the money"
c = a + b
print(c)

# String Format  --format()
date = 28
txt = "Today is {}"
print(txt.format(date))

qty = 3
itemno = 567
price = 50.45
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(qty, itemno, price))


price = 50.45
qty = 3
itemno = 567
myorder = "I want {2} pieces of item {1} for {0} dollars."
print(myorder.format(price,itemno,qty))


#Escape Character
# Backspace
abcd = "Hello \bWorld"
abcd = "Hello\tWorld"
print (abcd)
#techmr//
