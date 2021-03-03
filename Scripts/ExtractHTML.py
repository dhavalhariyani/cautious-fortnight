from bs4 import BeautifulSoup
import re
import requests

output = open("HTML_DATA.txt",'w')
#HTML data will be stores in this file

url = input("Enter URL :")

page = requests.get(url)
data = page.text

soup = BeautifulSoup(data,'html.parser')
output.write(soup.prettify())

output.close()
print ("\n\nALL DONE\n")