from bs4 import BeautifulSoup
from dateutil import parser
import urllib


def extractText(url, text):
    # extract the text from the link and append it to text
    try:
        page = urllib.request.urlopen(url).read()
    except urllib.error.HTTPError:
        extractText(url, text)

    soup = BeautifulSoup(page, 'lxml')
    try:
        headline = soup.find("h1", {"class" : "article-header"}).text
        date = soup.find("span", {"itemprop" : "datePublished"}).text
        content = soup.find("div", {"id" : "articleText"}).stripped_strings
    except AttributeError:
        return
    date = parser.parse(date)
    formattedDate='%s/%s/%s' % (date.month, date.day, date.year)
    pageInfo = list()
    pageInfo.append(headline)
    pageInfo.append(formattedDate)
    pageText = list()
    for paragraph in content:
        pageText.append(paragraph.replace('\xa0', ' ').replace("\'", "'").replace('\u0101', ' '))

    pageInfo.append(''.join(pageText))
    text.append(pageInfo)


def extractFromLinks(links):
    # Obtain each link and extractText from it
    text = list()
    
    # cycle through the links array
    for link in links:
        try:
            extractText(link, text)
        except urllib.error.HTTPError:
            continue
        
    return text
