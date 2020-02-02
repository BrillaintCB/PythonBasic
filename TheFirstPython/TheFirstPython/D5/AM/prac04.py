#*
#**
#***
#***
#**
#*

#my solution
for x in range(1,4,1):    
    print("*" * x)
    if(x>2):
        for y in range(3,-1,-1):
            print("*" * y)
            

#way2
star="*"
for i in range(0,2):
    for k in range(1,4):
        if i==0:
            print("{}".format(star*(i+k)))
        else:
            print("{}".format(star*(4-k)))

print()
print()


#way3

for y in range(1,7):
    for x in range(1,4):
        if y>=x and (y-x)<4:
            print("*",end="")

    print()

print()
print()




#way4