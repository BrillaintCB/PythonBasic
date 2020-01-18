
print("Please input number 10")
userinput = int(input())

sumOdd = 0
sumEven = 0
for i in range(1,userinput+1,1):
    if(i%2 == 0):
       sumEven += i
    else:
        sumOdd += i
print(sumOdd, sumEven)

