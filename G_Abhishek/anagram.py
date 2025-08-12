# Take input from the user
str1 = input("Enter the first string: ").lower().replace(" ", "")
str2 = input("Enter the second string: ").lower().replace(" ", "")

# Check if sorted characters of both strings are the same
if sorted(str1) == sorted(str2):
    print("The strings are anagrams!")
else:
    print("The strings are NOT anagrams.")
