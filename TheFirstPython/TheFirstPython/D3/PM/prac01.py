
day = 1
print(day not in range(1,32,1))
day = 32
print(day not in range(1,32,1))
day = -1
print(day not in range(1,32,1))
day = 33
print(day not in range(1,32,1))


ls = list(range(1,11,1))
ls = list(range(10,1,-1))

print(ls)

tp = tuple(range(1,11,1))
print(tp)



numlists = [1,2,3,4,5]
print("Please input number 3")
userinput = int(input())


#Ternary operators
if userinput in numlists:
    print("The number exist")
else:
    print("Not exist")



days = ["Monday","Tuseday","Wedseday","Thursday","Friday","Saturday","Sunday"]
fm = "You typed number {0} and it is {1}"
print("Please input number")
userInput = int(input())

if userinput not in range(1,32,1):
    print("Out of range")
else :
    day = days[(userInput % 7)-1]
    print(fm.format(userInput, day))

nums = [6,2,43,6800,5542,9,50,3]

print(14000+4000+6000+4500)