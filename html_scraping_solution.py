# OUTPUT: HTML file containing 
# Make an HTTP request to retrieve airline carrier and airport information
# and output an HTML file of what the site returns

from bs4 import BeautifulSoup
import requests
import json

s = requests.Session()

r = s.get('https://www.transtats.bts.gov/Data_Elements.aspx?Data=2')
soup = BeautifulSoup(r.text, "html5lib")
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
                   ("CarrierList", "AA"),
                   # ("CarrierList", "VX"),
                   ("AirportList", "MCO"),
                   # ("AirportList", "BOS"),
                   ("Submit", "Submit")
                  ))

# output_file = "E:/Google Drive/Backpack/Udacity DAND/04 Data Wrangling/virgin_and_logan_airport.html"
output_file = "E:/Google Drive/Backpack/Udacity DAND/04 Data Wrangling/american_and_orlando.html"
f = open(output_file,'w')
f.write(r.text)