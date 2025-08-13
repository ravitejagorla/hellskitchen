#Prime number.
# this will tell you if a given number is Prime number or not 
number = int(input("Enter a Number: "))


for i in range(2,number):
    if number % i == 0:
        print("Not a Prime number.")
        break
else :
    print("Prime number.")