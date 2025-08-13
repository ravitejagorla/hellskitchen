num=int(input("Enter number"))
if num>1:
    for x in range(2,num):
        if num%x==0:
            print("Not prime")
            break
    else:
        print("It is prime")
