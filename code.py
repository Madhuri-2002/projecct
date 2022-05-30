li=input("enter")
k=li.split(" ")
print(k)
def fun(i,j):
    if(k[i+1]=="zero"):
        print("0"*j,end="")
    elif(k[i+1]=="one"):
        print("1"*j,end="")
    elif(k[i+1]=="two"):
        print("2"*j,end="")    
    elif (k[i+1]=="three"):
        print("3"*j,end="")
    elif(k[i+1]=="four"):
        print("4"*j,end="")
    elif(k[i+1]=="five"):
        print("5"*j,end="") 
    elif(k[i+1]=="six"):
        print("6"*j,end="")
    elif(k[i+1]=="seven"):
        print("7"*j,end="")
    elif(k[i+1]=="eight"):
        print("8"*j,end="") 
    elif(k[i+1]=="nine"):
        print("9"*j,end="")
    else:
        print("fghj")    
    return
for i in range(len(k)):
    if(k[i]=="zero"):
        print("0",end="")
    elif(k[i]=="one"):
        print("1",end="")
    elif(k[i]=="two"):
        print("2",end="")    
    elif (k[i]=="three"):
        print("3",end="")
    elif(k[i]=="four"):
        print("4",end="")
    elif(k[i]=="five"):
        print("5",end="") 
    elif(k[i]=="six"):
        print("6",end="")
    elif(k[i]=="seven"):
        print("7",end="")
    elif(k[i]=="eight"):
        print("8",end="") 
    elif(k[i]=="nine"):
        print("9",end="")  
    elif(k[i]=="double"):
        j=1
        fun(i,j)
        i=i+3
    elif(k[i]=="triple"):
        j=2
        fun(i,j)
        i=i+3
        #fun(i)
    else:
        print("invalid")    
                                 