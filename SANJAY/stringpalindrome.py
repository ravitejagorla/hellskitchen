#String Palindrome
string1 = input("Enter a String: ").lower()

reversed_string = (string1[::-1])

if string1 == reversed_string:
    print("The given string is a Palindrome string.")
else:
    print("The given string is not a Palindrome string.")