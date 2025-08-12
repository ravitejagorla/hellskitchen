#Anagram of two strings

str1=input("Enter the String-1:").replace(" ","").lower()
str2=input("Enter the String-2:").replace(" ","").lower()
if sorted(str1)==sorted(str2):
    print("It is anagram")
else:
    print("It not is anagram")