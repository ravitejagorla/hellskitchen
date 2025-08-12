#String_Palindrome
import time
text = input("Enter a string: ")
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
print()
time.sleep(2)
print("End of the application")
print()