num, result,i = 0,0,1

while True:
    num=int(input("Number between 10~20\n"))
    if num<10 or num>20:
        print("please input again")
        continue
    else:
        while i<=num:
            result +=i;  i+=1
        else:
            print("1~", num, "sum of", result)
            break


