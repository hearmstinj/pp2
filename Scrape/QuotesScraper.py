import sys
import os
sys.path.append('../CSV/.')
from bs4 import BeautifulSoup
import urllib
from urllib import request
import time
import csv
from pathlib import Path


def getlastvalue(company):
    my_file = Path(r"../CSV/" + company + "_HistoricalQuotes.csv")
    if my_file.is_file() and os.path.getsize(str(my_file)) > 0:
        with open('../CSV/' + company + '_HistoricalQuotes.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            return next(reader)[0]
    else:
        return "2000/01/01"


def change_day(date):
    times = date.split()
    day = times[1]
    day = day[:len(day) - 1]
    if len(day) == 1:
        day = "0" + day
    return day


def writeToExistingCSV(text, symbol):
    fname = "../CSV/" + symbol + "_HistoricalQuotes.csv"
    with open(fname, "r+", encoding='utf-8', newline='') as file:
        old = file.read()
        file.seek(0)
        writer = csv.writer(file, delimiter=',')
        writer.writerows(text)
        file.write(old)


def writeToNewCSV(text, symbol):
    fname = "../CSV/" + symbol + "_HistoricalQuotes.csv"
    with open(fname, "w", encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(text)


def writetoHistoricalQuotes(ld, company):
    month_map = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                 "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    url = "https://www.google.com/finance/historical?q=NASDAQ%3A" + company + "&start=0&num=450"
    webpage = urllib.request.urlopen(url)
    soup = BeautifulSoup(webpage, 'lxml')
    table = soup.find('table', {"class": "gf-table historical_price"})
    data = table.stripped_strings
    skip_first = True
    counter = 0
    first_row = 0
    table = list()
    for string in data:
        if skip_first is True:
            first_row += 1
            if first_row == 6:
                skip_first = False
                row = list()
            continue
        if counter % 6 == 0:
            string = string.split()[2] + "/" + month_map[string[0:3]] + "/" + change_day(string)
        row.append(string)
        counter += 1
        if counter % 6 == 0:
            table.append(row)
            row = list()
    print(table)
    rows_to_add = list()
    for date in table:
        if date[0] != ld:
            rows_to_add.append([date[0], date[-2], date[1], date[2], date[3], date[5]])
        else:
            break
    print(rows_to_add)
    return rows_to_add


def generate_quotes(symbols):
    for symbol in symbols:
        lastdate = getlastvalue(symbol)
        new_rows = writetoHistoricalQuotes(lastdate, symbol)
        my_file = Path(r"../CSV/" + symbol + "_HistoricalQuotes.csv")
        if my_file.is_file():
            writeToExistingCSV(new_rows, symbol)
        else:
            writeToNewCSV(new_rows, symbol)

#generate_quotes(['aapl', 'amzn', 'csco', 'googl', 'msft', 'tsla'])
