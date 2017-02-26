from bs4 import BeautifulSoup
import urllib
from urllib import request
import time
import csv
import pandas as pd


def extractPage(url, links, lastlink):
    
    # set a timeout to overcome http request errors
    time.sleep(0.2)
    cpage = urllib.request.urlopen(url)

    soup = BeautifulSoup(cpage, 'lxml')
    linkSet = soup.find_all("span", {"class" : "fontS14px"})
    
    # only include internal links of nasdaq
    for span in linkSet:
        if (span.a['href'] + "\n") == lastlink:
            return 1
        if "nasdaq.com" in span.a['href']:
            links.append(span.a['href'])

    return 0


def extract(baseURL, nodeURL, symbol):
    
    url = nodeURL
    
    # obtain the last page number to navigate to and open the main news headlines page
    try:
        page = urllib.request.urlopen(baseURL)
    except urllib.error.HTTPError:
        extract(baseURL, nodeURL)
    info = BeautifulSoup(page, "lxml")
    lastNumber = int(info.find("a", {"id" : "quotes_content_left_lb_LastPage"})['href'][-2:])
    
    # create a list to store the links
    links = list()

    # check which was the last link opened, if any
    with open("../CSV/lastpagescanned.csv", "r") as file:
        for row in file:
            rowcontent = row.split(',')
            if rowcontent[0] == symbol:
                last_link_scanned = rowcontent[1]
    
    # Navigate through each page and append the links
    for pageIterator in range(1, lastNumber):
        try:
            if pageIterator == 1:
                flag = extractPage(url, links, last_link_scanned)
            else:
                flag = extractPage(url + str(pageIterator), links, last_link_scanned)
        except urllib.error.HTTPError:
            pageIterator -= 1
            continue
        if flag == 0:
            continue
        else:
            df = pd.read_csv("../CSV/lastpagescanned.csv", header=None)
            mat = df.as_matrix()
            for row in mat:
                if row[0] == symbol:
                    if len(links) > 1:
                        row[1] = links[0]
            with open("../CSV/lastpagescanned.csv", "w") as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerows(mat)
            return links
    return links
