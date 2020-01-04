#print("please input number")

#num = input()
#num2 = input()

#print("Addition two numbers are ", int(num)+int(num2))

print("What is the year today?")
thisyear = int(input())
print("Which year were you born?")
bornyear = int(input())

fm = "Current year is {0} and you were born in {1} so your age is {2}"

print("your age is", thisyear-bornyear)
#print(fm.format(str(thisyear), str(bornyear), thisyear-bornyear))
print(fm.format(thisyear, bornyear, thisyear-bornyear))
