# Take input from user
s = input("Enter a string to check if it's a palindrome: ")

# Convert the string to lowercase to make the check case-insensitive
s = s.lower()

# Check if the string is equal to its reverse
if s == s[::-1]:
    print("The string is a palindrome!")
else:
    print("The string is NOT a palindrome.")
