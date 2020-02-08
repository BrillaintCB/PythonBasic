# Num -> Binary num 

# format  -> n 


userInputNumber = 5

result = []
reservedResult = []

def getQuotientRemainder(num):    
    remainders = []    
    while(1==1):
        quotient = num // 2
        remainder = num % 2
        remainders.append(remainder)
        num = quotient
        if(quotient ==0):
            break
        else:
            continue
    return remainders

result.append(getQuotientRemainder(9))
result.append(getQuotientRemainder(20))
result.append(getQuotientRemainder(28))
result.append(getQuotientRemainder(18))
result.append(getQuotientRemainder(11))

for i in result:
    #if(i.count != userInputNumber):
    #    i.append(5)
    print(i)



#print(getQuotientRemainder(20))