list = [0,0,0,0]
lightCopy = list
deepCopy = list[:]


sum = 0


#list[0] = int(input("The first number: "))
#list[1] = int(input("The second number: "))
#list[2] = int(input("The third number: "))
#list[3] = int(input("The fourth number: "))



print("len() : ", len(list))

for i in range(len(list)):
    list[i] = int(input(str(i+1)+"Num: "))
    sum += list[i]

print(sum)

print(list[1:3])

print(list[0:3])
print(list[0:4])

print(list[2:])

print(list[:2])

print(id(list))

print(id(lightCopy))

lightCopy[2] = 2000
print(lightCopy[3])

print(list[2])


print(deepCopy[2])
    

import copy

deepCopyList = [10,20,30,40]

arr = copy.deepcopy(list)

arr[2] = 2000

print(id(list))
print(id(arr))
print("*"*50)
print(list[2])
print(arr[2])