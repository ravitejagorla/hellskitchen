a = int(input('Enter a number to know if it is Prime or not: '))

if a <= 1:
    print('The given number is not a prime number.')
else:
   
    is_prime = True
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            is_prime = False
            break

    if is_prime:
        print('The given number is a prime number!!!')
    else:
        print('The given number is not a prime number!!!')
