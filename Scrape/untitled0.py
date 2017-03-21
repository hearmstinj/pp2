# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:17:20 2017

@author: USER
"""

import sys
sys.path.append('../CSV/.')
from bs4 import BeautifulSoup
import urllib
from urllib import request
import time
import csv

def getlastvalue(company):
    with open('../CSV/' + company + '_HistoricalQuotes.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        #print (next(reader)[0])
        return (next(reader)[0])
        
def writetoHistoricalQuotes(lastdate, company):
    url = "http://nasdaq.com/symbol/" + company + "/historical"
    webpage = urllib.request.urlopen(url)
    soup = BeautifulSoup(webpage, 'lxml')
    id1 = soup.find("div", {"id": "historicalContainer"})
    print(id1)
    id2 = id1.find("div", {"id" : "quotes_content_left_pnlAJAX"})
    for table in id2:
        print(table)
    table = id1.find('table')   
    print(table)
    table_body = table.find('tbody')
    print(table_body)
    rows = table_body.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        date = cells[0].find(text=True)
        closingValue = cells[4].find(text=True)
        volume = cells[5].find(text=True)
        openingvalue = cells[1].find(text=True)
        highValue = cells[2].find(text=True)
        lowValue = cells[3].find(text=True) 
        print (closingValue)
            
    #with open('../CSV' + company + 'HistoricalQuotes.csv', 'w') as csvfile:
                
lastdate = getlastvalue('aapl')
writetoHistoricalQuotes(lastdate, 'appl')        
        
        
        
        
