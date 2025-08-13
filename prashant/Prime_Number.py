#program to check the given number is prime number or not
n=int(input("enter the number"))
if n<=0:
  print("enter valide number")
elif n==1:
  print("1 is not a prime number")
elif n==2:
  print("2 is only even prime number")
else:
  for i in range(2,n):
    if n%i==0:
      print(f"{n} is not prime number")
      break
  else:
    print(f"{n} is a prime number")