#문제

#홍길동은 A 은행에 예금통장을 만들었다. 

#이 예금 통장에 첫날에 10원을 예금하고, 

#다음날에는 전날의 2배인 20원을 예금하고, 

#세째날에는 40원을 예금하는 방식으로 30일간 매일 예금 하였다.

#홍길동이 10까지, 20일까지, 30일까지 각각 예금한 예금총액은 얼마인지 구하시오.

#(예금액은 첫날 10, 둘째날 20 , 셋째날 40, ... 2배씩 증가된다)

def calculate(day):
    sum = 0
    for i in range(1, day+1, 1):
        deposit = 10 * pow(2,i-1)
        sum += deposit
    print('{:20,}{:<20}' .format(sum,"원 입니다."))
calculate(1)
calculate(20)
calculate(30)


#Formula to calculate compound interest annually is given by:
#Compound Interest = P(1 + R/100)r
#Where,
#P is principle amount
#R is the rate and
#T is the time span
#(pow((1 + rate / 100), time)) 
#Python3 program to find compund 
#interest for given values.

def compound_interest(principle, rate, time):    
    CI = principle * (pow((1+rate/100), time))
    print("Compound interest", round(CI,3))

compound_interest(10000, 10.25, 5) 

