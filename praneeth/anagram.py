import time
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
print()
time.sleep(2)
print("End of the application")