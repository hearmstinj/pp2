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
        return next(reader)[0]

def writetoHistoricalQuotes(lastdate, company):
    dict = {'Jan' : '01', 'Feb' : '02', 'Mar' : '03', 'Apr' : '04', 'May' : '05', 'Jun' : '06',
        'Jul' : '07', 'Aug' : '08', 'Sep' : '09', 'Oct' : '10', 'Nov' : '11', 'Dec' : '12'}
    url = "https://www.google.com/finance/historical?q=NASDAQ%3A"+company
    webpage = urllib.request.urlopen(url)
    soup = BeautifulSoup(webpage, 'lxml')
    table = soup.find('table', {"class": "gf-table historical_price"})
    data = table.stripped_strings
    lst = list(data)
    i = 6
    while(i < len(lst)):
        date = lst[i]
        closingValue = lst[i+4]
        Volume = lst[i+5]
        openingValue = lst[i+1]
        lowValue = lst[i+3]
        highValue = lst[i+4]
        month = date[0:3]
        if(len(date) == 12):
            year = date[8:12]
            day = date[4:6]
        else:
            year = date[7:11]
            day = date[4:5]
        if(len(day) == 1):
            actualDate = year+"/"+dict[month]+"/"+"0"+day
        else:
            actualDate = year+"/"+dict[month]+"/"+day
        print(actualDate)
        i = i+6
        
lastdate = getlastvalue('aapl')
writetoHistoricalQuotes(lastdate, 'aapl')