# Prime number or not

number=int(input("Enter the number:"))
for i in range(2,number):
    if number%i==0:
        print(number,":it is not a prime number")
        break
else:
    print(number,": it is a prime number")



# range of prime numbers

number1=int(input("Enter the number1:"))
for i in range(2,number1+1):
    for j in range(2,i):
        if i % j == 0 :
            break
    else:
        print(i,":This are prime numbers")


        