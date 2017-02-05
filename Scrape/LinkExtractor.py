from bs4 import BeautifulSoup
import urllib
from urllib import request
import time

def extractPage(url, links):
    
    #set a timeout to overcome http request errors
    time.sleep(0.2)
    cpage = urllib.request.urlopen(url)

    soup = BeautifulSoup(cpage, 'lxml')
    linkSet = soup.find_all("span", {"class" : "fontS14px"})
    
    #only include internal links of nasdaq    
    for span in linkSet:
        if "nasdaq.com" in span.a['href']:
            links.append(span.a['href'])
    
def extract(baseURL, nodeURL):
    
    url = nodeURL
    
    #obtain the last page number to navigate to and open the main news headlines page
    page = urllib.request.urlopen(baseURL)
    info = BeautifulSoup(page, "lxml")
    lastNumber = int(info.find("a", {"id" : "quotes_content_left_lb_LastPage"})['href'][-2:])
    
    #create a list to store the links
    links = list()
    
    #obtain the links from the first page
    extractPage(baseURL, links)
    
    #Navigate through each page and append the links
    for pageIterator in range(2, lastNumber):
        try:
            extractPage(url + str(pageIterator), links)
        except urllib.error.HTTPError:
            pageIterator -= 1
            continue

    return links
