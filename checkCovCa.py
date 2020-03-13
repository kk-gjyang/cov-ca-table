#!/usr/bin/python3

# chmod +x checkCovCa.py
# crontab -e
# * * * * * cd /PATH/TO/APP_FOLDER && ./checkCovCa.py

from bs4 import BeautifulSoup
from requests_html import HTMLSession

caDataFile = "caData.txt"
session = HTMLSession()
r = session.get('https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19.html')
r.html.render()

soup = BeautifulSoup(r.html.html, 'html.parser')
newData = str(soup.find('table'))

f = open(caDataFile, "r")
savedData = f.read()
f.close

if newData != savedData:
  f = open(caDataFile, "w")
  f.write(newData)
  f.close