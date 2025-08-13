str1 = input("Enter a string: ")
str2 = input("Enter a string: ")

anagram_str1 = str1.replace(" ","").lower()
anagram_str2 = str2.replace(" ","").lower()

if len(anagram_str1) != len(anagram_str2):
    print("Given strings are not Anagram strings.")

elif sorted(anagram_str1) == sorted(anagram_str2):
    print("GIven Strings are Anagram strings.")

else:
    print("Given Strings are Not Anagram strings.")