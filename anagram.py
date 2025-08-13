L1=input("enter L1 ").lower()
L2=input("enter L2").lower()
L1=L1.replace("","")
L2=L2.replace("","")
if sorted(L1)==sorted(L2):
    print("They are anagram")
else:
    print("They are not anagram")
     
