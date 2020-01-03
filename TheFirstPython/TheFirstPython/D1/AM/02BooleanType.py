#Boolean Values

print("\'single\'== \"Sinlge\"", 'single'=="single") #true

print("int(5.5) == 5" ,int(5.5)==5) #true

print("float(5) == int(5)" ,float(5)==int(5)) #true
print("\"5\" == int(5)","5"==int(5)) #false

a = int(200)
b = float(55.5)

if b>a:
    print("b>a")
else:
    print("b<a")

"""
Some Values are False
In fact, there are not many values 
that evaluates to False, 
except empty values, 
such as (), [], {}, "", 
the number 0, and the value None.
And of course the value False evaluates to False.
"""


mylist = ["apple", "bannaa", "orange"]
x = len(mylist)
print("true expected",bool(x))  #true

print("true expected ",bool("abc")) #true

print("false expected ",bool(0))

