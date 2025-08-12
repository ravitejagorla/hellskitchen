a=int(input("Enter any number: "))
for i in range(2,a+1):
    pr=True
    for j in range(2,i):
        if i%j==0:
            pr=False
            break
    if pr:
        print(i,end=" ")