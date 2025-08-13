value1=input("Enter First value:").lower()
value2=input("Enter Second value:").lower()
value1=value1.replace(" "," ")
value2=value2.replace(" "," ")
if sorted(value1)==sorted(value2):
    print("The values are anagrams.")
else:
    print("The values are not anagrams.")