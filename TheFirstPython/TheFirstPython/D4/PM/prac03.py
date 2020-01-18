
print("Please input two numbers \nFirst number")
userinput = int(input())
print("Please input the second number")
userinput2 = int(input())

fmt = "3*x and 7*x"
tot = 0
for i in range(1,101,1):
    if(i%3 == 0 and i%7 ==0):
        print(fmt, i)
        tot += i 


print("Total sum" ,tot)