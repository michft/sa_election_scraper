#!/usr/bin/python3

from bs4 import BeautifulSoup

import requests

""" Simple scraper to get the 2PP from the SA election website."""

url = "http://www.ecsa.sa.gov.au/elections/2014-state-election-results-summary/house-of-assembly-district-results/districtsummary/"

print ("Division, Candidate, Affiliation, Percentage, %, Ballot Papers")

for i in range(701,748):
  r  = requests.get(url +str(i))
  data = r.text
  soup = BeautifulSoup(data)
  divis = soup.find('strong')
  for tabuladata in soup.find_all('table'):
    tablebody = tabuladata.find('tbody')
    if len(tablebody.find_all('tr')) == 2:
      # Only interested in 2PP
      for tabrow in tablebody.find_all('tr'):
        print(divis.get_text(), ', ' , end=' ')
        for tabledata in tabrow.find_all('td'):
          if tabledata.find_all('br'):
            # There is a better way, it's 1am and this is clean enough.
            print(tabledata ,', ', end=' ')
          else:
            print(tabledata.get_text().replace('\n', ' ' ) , ', ', end=' ' )
        print()
