str = "Hello World Let's move to Australia!"

e_count = a_count = 0


for i in str:
    if(i == 'e'):
        e_count +=1
    elif(i == 'a'):
        a_count +=1


result = "{0}, {1}"
print(result.format(e_count, a_count))