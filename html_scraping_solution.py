from bs4 import BeautifulSoup
import requests
import json

s = requests.Session()

r = s.get('https://www.transtats.bts.gov/Data_Elements.aspx?Data=2')
soup = BeautifulSoup(r.text)
viewstate = soup.find(id='__VIEWSTATE')['value']
eventvalidation = soup.find(id='__EVENTVALIDATION')['value']
viewstategenerator = soup.find(id='__VIEWSTATEGENERATOR')['value']

r = s.post("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
           data = (
                   ("__EVENTTARGET", ""),
                   ("__EVENTARGUMENT", ""),
                   ("__VIEWSTATE", viewstate),
                   ("__VIEWSTATEGENERATOR",viewstategenerator),
                   ("__EVENTVALIDATION", eventvalidation),
                   ("CarrierList", "VX"),
                   ("AirportList", "BOS"),
                   ("Submit", "Submit")
                  ))

output_file = "E:/Google Drive/Backpack/Udacity DAND/04 Data Wrangling/virgin_and_logan_airport.html"
f = open(output_file,'w')
f.write(r.text)