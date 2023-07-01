#Let us make a basic calculator!
#This is still under working!!
from time import sleep
print("Chalo bhai karte hai calculate...")
sleep(1)

while True:
    x, a, y, b = float(input("Enter first number ")), input("Write first operator '+,-,*,/' "), float(input("Enter second number ")), input("Write second operator or type 'r' for result ")
    
    if a == "+":
        R = float(x + y)
        if b == "r":
            print("Answer: ",R)
            cont = input("Press any key to continue...")
        
    #system for third number
        if b == "+":
            z = float(input("Write third number: "))
            r = float(x + y + z)
            print("Answer: ",r)
            cont = input("Press any key to continue...")
            
        elif b == "-":
            z = float(input("Write third number: "))
            r = float(x + y - z)
            print("Answer: ",r)
            cont = input("Press any key to continue...")
        elif b == "*":
            z = float(input("Write third number: "))
            r = float(x + y * z)
            print("Answer: ",r)
        elif b == "/":
            z = float(input("Write third number: "))
            r = float(x + y / z)
            print("Answer: ",r)
            cont = input("Press any key to continue...")
        continue
    elif a == "-":
        R = float(x - y)
        if b == "r":
            print("Answer: ",R)
            cont = input("Press any key to continue...")
    #system for third number
        if b == "+":
            z = float(input("Write third number: "))
            r = float(x - y + z)
            print("Answer: ",r)
            cont = input("Press any key to continue...")
        elif b == "-":
            z = float(input("Write third number: "))
            r = float(x - y - z)
            print("Answer: ",r)
            cont = input("Press any key to continue...")
        elif b == "*":
            z = float(input("Write third number: "))
            r = float(x - y * z)
            print("Answer: ",r)
            cont = input("Press any key to continue...")
        elif b == "/":
            z = float(input("Write third number: "))
            r = float(x - y / z)
            print("Answer: ",r)
            cont = input("Press any key to continue...")
        continue
    elif a == "*":
        R = float(x * y)
        if b == "r":
            print("Answer: ",R)
            cont = input("Press any key to continue...")
    #system for third number
        if b == "+":
            z = float(input("Write third number: "))
            r = float(x * y + z)
            print("Answer: ",r)
            cont = input("Press any key to continue...")
        elif b == "-":
            z = float(input("Write third number: "))
            r = float(x * y - z)
            print("Answer: ",r)
            cont = input("Press any key to continue...")
        elif b == "*":
            z = float(input("Write third number: "))
            r = float(x * y * z)
            print("Answer: ",r)
            cont = input("Press any key to continue...")
        elif b == "/":
            z = float(input("Write third number: "))
            r = float(x * y / z)
            print("Answer: ",r)
            cont = input("Press any key to continue...")
        continue
    elif a == "/":
        R = float(x / y)
        if b == "r":
            print("Answer: ",R)
            cont = input("Press any key to continue...")
    #system for third number
        if b == "+":
            z = float(input("Write third number: "))
            r = float(x / y + z)
            print("Answer: ",r)
            cont = input("Press any key to continue...")
        elif b == "-":
            z = float(input("Write third number: "))
            r = float(x / y - z)
            print("Answer: ",r)
            cont = input("Press any key to continue...")
        elif b == "*":
            z = float(input("Write third number: "))
            r = float(x / y * z)
            print("Answer: ",r)
            cont = input("Press any key to continue...")
        elif b == "/":
            z = float(input("Write third number: "))
            r = float(x / y / z)
            print("Answer: ",r)
            cont = input("Press any key to continue...")
        continue
    elif b == "r":
        print("Write operator carefully...")
        cont = input("Press any key to continue...")
        continue
