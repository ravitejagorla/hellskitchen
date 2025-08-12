#String palindrome

string1=input("Enter Any string:")
string2=string1[::-1]
if string1==string2:
    print(string1,":It is palindrome")
else:
    print(string1,":It Not is palindrome")