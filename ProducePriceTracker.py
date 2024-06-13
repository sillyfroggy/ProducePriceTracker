import requests
from bs4 import BeautifulSoup
from vegtoprice import vegtoprice
import os

url = "https://www.foodcoop.com/produce/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

if 'veggies.txt' in os.listdir():
    with open("veggies.txt", "w") as v:
        for veg in soup.find_all("tr"):
            v.write(str(veg))
    
    v.close()

veggie = input("Search for which veggie? ")

veggie = veggie[0].upper() + veggie[1:].lower()
        
vegtoprice(veggie)