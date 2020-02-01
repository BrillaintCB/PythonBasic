str = "{0:1} * {1:1} = {2:2}"

#print('{:20,}{:<20}' .format(sum,"원 입니다."))

for i in range(1,10):
    for j in range(1,10):
        if(j==9 or j==5):
             print(str.format(i,j, i*j),end="\n")
        else:
            print(str.format(i,j, i*j), end="\t")
                    