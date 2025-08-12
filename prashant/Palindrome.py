#program to check the given string is palindrome or not
def Palindrome():
  a=input("enter the string here")
  b=a[::-1]
  if a==b:
    print(f"{a} is a palindrome")
  else:
    print(f"{a} not a palindrome")
Palindrome()