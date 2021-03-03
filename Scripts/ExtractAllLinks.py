# Fetch all the links from webpage and store it into a text file
from bs4 import BeautifulSoup
import re
import requests

url = input("Enter URL : ")
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data,'html.parser')
output = open("ExtractedLinks.txt",'w')
for a in soup.find_all('a', href=True):
	output.write(a['href']+ '\n')		
output.close()

print ("\n\nALL DONE\n")