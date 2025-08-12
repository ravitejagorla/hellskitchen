#Prime number.
# this will tell you if a given number is Prime number or not 
number = int(input("Enter a Number: "))


for i in range(2,number):
    if number % i == 0:
        print("Not a Prime number.")
        break
else :
    print("Prime number.")




#Prime number.

# this will print number of prime numbers 
# number = int(input("Enter a Number: "))

prime_number = []

for a in range(2,number + 1):
    for b in range(2,a):

        if a % b == 0:
            break
    else :
        prime_number.append(a)

print("These are the prime numbers :", prime_number)


    
