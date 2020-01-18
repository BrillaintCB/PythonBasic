
print("Please input two numbers \nFirst number")
userinput = int(input())
print("Please input the second number")
userinput2 = int(input())

for i in range(userinput, userinput2+1, 1):
    if(i%7 == 0):
        print(i, end=" ")

