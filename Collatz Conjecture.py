x=10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000099999999999999999999999999999999999999999999999999999999999999999999999999999
for i in range(1,x,1):
    print(i)
    if (i==1):
        print("True")
        continue        
    if (i<1):
        print("Invalid")
        continue
    if (i>1):
        while (i!=1):
           if ((i%2)==0):
               i=i/2
           elif ((i%2)!=0):
               i=3*i+1
        print("True")
        

    
                    
    
