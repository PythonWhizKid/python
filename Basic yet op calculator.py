#Let us make a basic calculator!
#This is still under working!!
from time import sleep
print("Chalo bhai karte hai calculate...")
#sleep(1)
x, a, y, b = float(input("Enter first number ")), input("Write first operator '+,-,*,/' "), float(input("Enter second number ")), input("Write second operator or type 'r' for result ")
#system for third number
if b == "r" and a == "+":
    R = float(x + y)
    print("Answer: ",R)
elif b == "r" and a == "-":
    R = float(x - y)
    print("Answer: ",R)
elif b == "r" and a == "*":
    R = float(x * y)
    print("Answer: ",R)
elif b == "r" and a == "/":
    R = float(x / y)
    print("Answer: ",R)
elif b == "r":
    print("Write operator carefully...")
