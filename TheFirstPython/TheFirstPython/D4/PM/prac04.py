cnt = 0

while cnt<5:
    print("3 / 4 ?")
    userinput = int(input())

    fmt3 = "{0} is multiply of 3"
    fmt4 = "{0} is multiply of 4"

    for i in range(1,userinput+1,1):
        if (i % 3 == 0):
            fmt3.format(userinput)

    cnt += 1







#    num = int(input('정수 입력 : '))
#if num == 0 :
#print(num,"은(는) 3의 배수도 4의 배수도 아닙니다");
#elif num % 3 == 0 and num % 4 == 0 :
## elif num % 12 == 0 : 이와 같은 조건식을 설계해도 결과는 동일함
#print(num,"은(는)3의 배수 이면서,4의 배수입니다");
#elif num %3 == 0:
#print(num,"은(는)3의 배수 입니다");
#elif num %4 == 0:
#print(num,"은(는)4의 배수 입니다");
#else:
#print(num,"는 3의 배수도 4의 배수도 아님");