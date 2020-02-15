#"""
#Taxi
#"""

#문제

#비행기를 타는데 30분 거리까지의 기본 요금은 30000원이며, 

#10분 단위로 추가요금 5000원씩 부가됩니다. 

#비행기 탑승 시간을 입력받아서 시간에 의하여 요금을 계산하는

#요금 계산기 프로그램을 작성하세요.



#*코딩조건*

#if, else, elif 등의 조건문을 반드시 사용하세요. 

#입력받은 분단위의 시간을 연산식으로 세워서 요금을 계산하여야 합니다.
#실행결과에 표시된 탑승 시간 이외에 모든 탑승 시간이 완벽하게
#연산식에 의해서 계산이 되어야 합니다.

#*실행결과*


#비행기 탄 시간(분): 29

#30,000 원 입니다.

#비행기 탄 시간(분): 31

#30,000 원 입니다.

#비행기 탄 시간(분): 39

#30,000 원 입니다.

#비행기 탄 시간(분): 40

#35,000 원 입니다.

#비행기 탄 시간(분): 42

#35,000 원 입니다.

#비행기 탄 시간(분): 50

#40,000 원 입니다.

## 실습-0-1 해답

#money = 30000
#time = int(input("비행기 탄 시간(분): ")) # 시간을 입력받음
#time -= 30 # 입력한 시간에서 30분을 차감하여 저장함
## 차감하는 이유는 기본 요금을 계산하기 위한것임
#if time > 0:
#    money = money + time // 10 * 5000
#     # 30분 초과의 탑승시간이 10으로 나누어 떨어지는 경우의 요금을 계산함
#     # 10분단위 추가요금을 감안한 요금을 계산함
#print('{:6,}{:<6}' .format(money,"원 입니다."))