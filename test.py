"""import time 
x1=10
print("x1_value is:",x1)
print("the data type is:",type(x1))
print()
x2=20
print("x2_value is:",x2)
print("the data type is:",type(x2))
print()
res1=x1+x2
print("add two values:",x1+x2)
print()
time.sleep(2)
print("end of an appliction")""



""""""import time
y1=134.11
print("y1_value is:",y1)
print("the data type is:",type(y1))
print()
y2=140.12
print("y2_value is:",y2)
print("the data type is:",type(y2))
print()
res1=y1*y2
print("add two values:",res1)
print()
time.sleep(2)
print("end of an application")""""""


""""""import time 
X1=1.3E1
print("X1_value is:",X1)
print()
print("The data type is:",type(X1))
print()
time.sleep(2)
print("End of an application")"""

"""import time 
X1=1.3*10*10
print("X1_value is:",X1)
print()
print("The data type is:",type(X1))
print()
time.sleep(2)
print("End of an application")"""




"""import time 
X1=10000 
X2=20000 
print("====Using_Boolean_Data_Type====")
print(X1," ",X2)
print()
res1=X1==X2 
res2=X1!=X2 
print(res1," ",type(res1))
print()
print(res2," ",type(res2))
print()
time.sleep(2)
print("End of an application")"""


"""import time
y1=10000
y2=200000
print("===using boolean data type===")
print(y1," ",y2)
print()
res1=y1!=y2
res2=y1==y2
print(res1," ",type(res1))
print(res2," ",type(res2))
print()
time.sleep(2)
print("end of an appliction")"""


"""import time
a=10
b=30
print("===using boolean data type===")
c=a<b
print(type(c))
time.sleep(2)
print(a>b)"""

"""import time
str1='sreekar'
str2="indhra"
str3='''sai'''
str4='10'
str5="200.4"
str6='''true'''
print(str1)
print(type(str1))
print(str2)
print(type(str2))
print(str3)
print(type(str3))
print(str4)
print(type(str4))
print(str5)
print(type(str5))
print(str6)
print(type(str6))
time.sleep(2)
print("end of an applicatiom")"""



"""import time
L1=[]
print(type(L1))
L1=20,30
print(L1)
time.sleep(2)
print("end of an application")"""

"""import time
L1=[10]
L1.append(10)
print(type(L1))
print(L1)
time.sleep(2)
print("end of an application")"""


"""import time 
X1=input("Enter the X1_value:")
print(X1)
print()
print(type(X1))
print()
time.sleep(2)
print("End of an application")"""

"""import time 
print("====Before_Typecasting")
X1=input("Enter the X1_value:")
X2=input("Enter the X2_value:")
res1=X1+X2 
print(X1," ",type(X1))
print()
print(X2," ",type(X2))
print()
print(res1," ",type(res1))
print()
print("====After_Typecasting")
X1=int(input("Enter the X1_value:"))
X2=int(input("Enter the X2_value:"))
res1=X1+X2 
print(X1," ",type(X1))
print()
print(X2," ",type(X2))
print()
print(res1," ",type(res1))
print()
time.sleep(2)
print("End of an application")"""


"""import time
x1=[2,9,3,5,7,6]
print(type(x1))
print()
print("===Removing objects")
x1.remove(2)
x1.remove(6)
print(x1)
time.sleep(2)
print("end of an application")"""


"""import time
x1=[1,1,2,7,3,2]
print(type(x1))
print()
print("===Removing duplicate objects")
x1.remove(1)
x1.remove(2)
print(x1)
time.sleep(2)
print("end of an application")"""

"""import time
x1="python"
print(type(x1))
print("Reversing of a string:",x1[::-1])
print()
time.sleep(2)
print("end of an application")"""

"""X="sreekar"
y=""
for i  in X:
    y=i+y
    print(y)"""

"""import time 
X1=eval(input("X1_value:"))
X2=eval(input("X2_value:"))
res1=X1*X2 
print("The result_set of SR is:",res1)
print()
time.sleep(2)
print("End of an application")"""


"""name=eval(input("enter the name:"))
age=eval(input("enter the age:"))
if (name=="python" and age==96):
    print("hi")"""

"""a=[1,2,3,4,5]
for i in a:
    print(i)"""


"""b="sreekar"
for s in b:
    print(s)"""

"""while True:
    print("hi")"""

"""for i in range(0,20):
    for j in range(0,20):
        print(i==j)"""

# while True:
#     print("malli")





"""import webbrowser

# Message to send
message = "sreekar"
# WhatsApp link with the message
whatsapp_link = f"https://wa.me/?text={message.replace(' ', '%20')}"
print("Click the link to send your message on WhatsApp:", whatsapp_link)

# Automatically open the link in the default web browser
webbrowser.open(whatsapp_link)"""


# Love shape with numbers
"""for row in range(6):
    for col in range(7):
        if ((row == 0 and col % 3 != 0) or
            (row == 1 and col % 3 == 0) or
            (row - col == 2) or
            (row + col == 8)):
            print(row + 1, end=" ")
        else:
            print(" ", end=" ")
    print()"""



"""for raw in range(100):
    for col in ramnge(200):
        if ((raw == 10 and col %30 !=10) or
             (raw == 20 and col % 30 == 0) or
             (raw - col == 20) or
             (raw = col == 80):
             print(raw + 10, end = "")
        else:
            print(" ", end ="")
            print()"""


# Man shape using for loops
"""for row in range(7):
    for col in range(7):
        if (row == 0 and col == 3) or \
           (row == 1 and (col == 2 or col == 3 or col == 4)) or \
           (row == 2 and col == 3) or \
           (row == 3 and (col == 1 or col == 3 or col == 5)) or \
           (row == 4 and (col == 0 or col == 3 or col == 6)) or \
           (row == 5 and (col == 2 or col == 4)) or \
           (row == 6 and (col == 1 or col == 5)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()"""






