#Let us make a basic calculator!
#This is still under working!!
from time import sleep
print("Chalo bhai karte hai calculate...")
sleep(1)
x, a, y, b = float(input("Enter first number ")), input("Write first operator '+,-,*,/' "), float(input("Enter second number ")), input("Write second operator or type 'r' for result ")

if a == "+":
    R = float(x + y)
    if b == "r":
        print("Answer: ",R)
    #system for third number
    if b == "+":
        z = float(input("Write third number: "))
        r = float(x + y + z)
        print("Answer: ",r)
    elif b == "-":
        z = float(input("Write third number: "))
        r = float(x + y - z)
        print("Answer: ",r)
    elif b == "*":
        z = float(input("Write third number: "))
        r = float(x + y * z)
        print("Answer: ",r)
    elif b == "/":
        z = float(input("Write third number: "))
        r = float(x + y / z)
        print("Answer: ",r)
elif a == "-":
    R = float(x - y)
    if b == "r":
        print("Answer: ",R)
    #system for third number
    if b == "+":
        z = float(input("Write third number: "))
        r = float(x - y + z)
        print("Answer: ",r)
    elif b == "-":
        z = float(input("Write third number: "))
        r = float(x - y - z)
        print("Answer: ",r)
    elif b == "*":
        z = float(input("Write third number: "))
        r = float(x - y * z)
        print("Answer: ",r)
    elif b == "/":
        z = float(input("Write third number: "))
        r = float(x - y / z)
        print("Answer: ",r)
elif a == "*":
    R = float(x * y)
    if b == "r":
        print("Answer: ",R)
    #system for third number
    if b == "+":
        z = float(input("Write third number: "))
        r = float(x * y + z)
        print("Answer: ",r)
    elif b == "-":
        z = float(input("Write third number: "))
        r = float(x * y - z)
        print("Answer: ",r)
    elif b == "*":
        z = float(input("Write third number: "))
        r = float(x * y * z)
        print("Answer: ",r)
    elif b == "/":
        z = float(input("Write third number: "))
        r = float(x * y / z)
        print("Answer: ",r)
elif a == "/":
    R = float(x / y)
    if b == "r":
        print("Answer: ",R)
    #system for third number
    if b == "+":
        z = float(input("Write third number: "))
        r = float(x / y + z)
        print("Answer: ",r)
    elif b == "-":
        z = float(input("Write third number: "))
        r = float(x / y - z)
        print("Answer: ",r)
    elif b == "*":
        z = float(input("Write third number: "))
        r = float(x / y * z)
        print("Answer: ",r)
    elif b == "/":
        z = float(input("Write third number: "))
        r = float(x / y / z)
        print("Answer: ",r)
elif b == "r":
    print("Write operator carefully...")
