row = 1
while(row!=0):
    row=int(input("0. Exit , 1. Continue\n"))
    if(row==0):
        print("Program exits\n")
        break;
    else:
        num=int(input("Input odd number which is greater than 2\n"))
        if(num<3 or num%2 == 0):
            print("Please try again\n")
        else:
            for n in range(1,num+1,1):               
                temp = 2*n-1
                print('{:^30}'.format(temp * "*"))
                if(num == n):
                    for i in range(n-1, 0,-1):
                        temp1 = 2*i-1
                        print('{:^30}'.format(temp1* "*"))





#while(row!=0):
#    row=int(input("0. Exit , 1. Continue\n"))
#    if(row==0):
#        print("Program exits\n")
#        break;
#    else:
#        num=int(input("Input odd number which is greater than 2\n"))
#        if(num<3 or num%2 == 0):
#            print("Please try again\n")
#        else:
#            for n in range(1,num+1,1):               
#                temp = 2*n-1
#                #print(temp)
#                print('{:^15}'.format(temp * "*"))
#                if(num == 2*n-1):
#                    #print(num,n)
#                    #print("10 -> n = 5,  2n -1 = 9  ")
#                    for i in range(n-1, 1,-1):
#                        temp1 = 2*i-1
#                        #print(i)
#                        print('{:^15}'.format(temp1* "*"))
                        
#                   #for i in range(num,num/2,-):
#                     #  print(i * "*")
                       
                       
                

    







                     

                       






#for x in range(1,4,1):    
#    print("*" * x)
#    if(x>2):
#        for y in range(2,-1,-1):
#            print("*" * y)