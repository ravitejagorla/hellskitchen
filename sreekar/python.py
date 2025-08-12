def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def are_anagrams(a, b):
    return sorted(a.replace(" ", "").lower()) == sorted(b.replace(" ", "").lower())