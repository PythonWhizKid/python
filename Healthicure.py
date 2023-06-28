#Lets create a BMI calculator with feedback support
#Also user can choose which unit to put height in
from time import sleep
print("Welcome to Healthicure...")
sleep(1)
Name = input("What is your good name? ")
sleep(1)
print(Name, " is certainly a sweet name")
sleep(1)
print("Lets calculate your BMI...")
sleep(1)
W = float(input("Enter weight in kilograms "))
sleep(1)
print("Perfect...")
sleep(1)
U = str(input("Write 'cm', if you know your height in centimetres and 'm' for metres... "))
sleep(1)
H = float(input("Enter your height in "+ U ))
#we used plus above so that we can combine the three arguments into one (Enter..height, U and %)
sleep(1)
print("Please wait while we process the data...")
sleep(1)
if U == "cm":
    BMI = W*10000/(H**2)
elif U == "m":
    BMI = W/(H**2)
else:
    print("Try again! ")
print("Your BMI is... ", float(BMI))
sleep(1)

#Feedback
if BMI >= 18.5 and BMI <= 24.9:
    print("Your BMI is normal... Stay Healthy")
    sleep(1)
    print("Thanks for using Healthicure!")
elif BMI < 18.5:
    print("You are currently underweight... ")
    sleep(1)
    print("Thanks for using Healthicure!")
elif BMI > 24.9 and BMI < 40:
    print("You are currently overweight...")
    sleep(1)
    print("Thanks for using Healthicure!")
elif BMI >= 40:
    print("You are currenlty obese...")
    print("Thanks for using Healthicure!")
else:
    print("Please enter details correctly...")
  
