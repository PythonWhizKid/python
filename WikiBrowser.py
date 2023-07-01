#Developed by @PythonWhizKid
#python3
import requests
from bs4 import BeautifulSoup
from time import sleep

print("Welcome to WikiBrowser by @PythonWhizKid")

sleep(2)

#si = input("Please use '_' for spaces. Type Topic: ")
#update July 1, 2023
si = input("Type topic: ")
sii = si.replace(" ", "")
url = ("https://en.wikipedia.org/wiki/" + sii)
#update done
#url = ("https://en.wikipedia.org/wiki/" + si)

# get the html
r = requests.get(url)
htmlContent = r.content
# use the command to view html code of page - print (htmlContent)
# Parse the html

soup = BeautifulSoup(htmlContent, 'html.parser')

#to print all the paras text
for para in soup.find_all("p"):
    print(para.get_text())
print("ThankYou for Using... Program developed by @PythonWhizKid")
Rating = int(input("Rate your experience (from 1 to 5): "))

if Rating == (1 , 2 , 3 , 4 , 5):
    print("Thanks for using")
    
exit
