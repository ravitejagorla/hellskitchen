number = int(input("Enter a number:"))
if number<=1:
    print("the number is not prime")
else:
    for i in range(2,number):
        if number%i == 0:
            print("the number is not a prime number:")
            break
    else:
            print("thr number is prime")
