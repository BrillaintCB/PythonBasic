


menuDict = dict()
menuDict["Coffee"] = 200
menuDict["Coke"] = 250
userMoney = 0
menuLists = []

while(True):
    print("Please Insert money")
    userMoney += int(input())

    print("1. Coffee(200)	2. Coke(250)	3. Return	4. Exit $",userMoney)
    userInput = int(input())


    if(userInput==4):
        print("The program ends")    
        break;
    elif(userInput==1 or userInput==2):
       if(userInput==1 and userMoney>= menuDict["Coffee"]):
           userMoney -= menuDict["Coffee"]
           print("Enjoy your balance is $",userMoney)
       elif(userInput==2 and userMoney>= menuDict["Coke"]):
           userMoney -= menuDict["Coke"]
           print("Enjoy your balance is $",userMoney)
       else:
           print("Your balance is shortage please insert more money")
    else:
        print("Out of range")
    