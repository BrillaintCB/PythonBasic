
print("          %d" % 123)
#print("%d %d" %123)

print("%d          %d" %(123, 321))

print("%d + %d =        %d" % (123,321, 123+321))


print("*"*50)


a = "right"
b = "left"
str = "{:>20}"
strl = "{:<20}"
strc = "{:^20}"
#c style
print('% 10d\n %10d' % (10000,200000))
#python


"""
Print fixxed length
"""
#c style
print('%5d %05d' %(1,1))
#python
print('{:5} {:05}'.format(1,1))


print(strl.format('$'+"1000000"))
print(strl.format('$'+"100000"))

print(str.format(1000000))
print(str.format(100000))

#strcomma = "{:}"

#strcomma = "{:,}"
strcomma = "{: >20,.2f}"
print("#"*50)
print(strcomma.format(10000000.5555555))
print("#"*50)
print("*"*50)
print(str.format(strcomma.format(10000000.5555555)))
print(strc.format(strcomma.format(10000000.5555555)))
print("*"*50)

print(strcomma.format(2000))



#strcomma = "{: >20,.2f}"

#ex !!!python!!! (12)
answer = "!!!python!!!"
print(len(answer))


ex1 = "python"
f = "{0:!^12}"
print(f.format(ex1))




