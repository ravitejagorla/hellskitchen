# Prime number 
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(s):
    print("== Palindrome ==")
    return s == s[::-1]
def is_anagram(str1, str2):
    print("== anagram ==")
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())

if __name__ == "__main__":
    num = int(input("Enter a number to check if it's prime: "))
    print(num, "is prime;", is_palindrome(num))

    text = input("Enter a string to check if it's a palindrome: ")
    print(text, "is a palindrome:",is_palindrome(text))

    str1 = input("Enter the first string : ")
    str2 = input("Enter the second string : ")
    print(str1," ",str2, "are anagrams:", is_anagram(str1, str2))
