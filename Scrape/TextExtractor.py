from bs4 import BeautifulSoup
import urllib

def extractText(url, text):
    #extract the text from the link and append it to text
    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page, 'lxml')
    try:
        headline = soup.find("h1", {"class" : "article-header"}).text
        date = soup.find("span", {"itemprop" : "datePublished"}).text
        content = soup.find("div", {"id" : "articleText"}).stripped_strings
    except AttributeError:
        return
    pageInfo = list()
    pageInfo.append(headline)
    pageInfo.append(date)
    for paragraph in content:
        pageInfo.append(paragraph.replace('\xa0', ' ').replace("\'", "'"))
        
    text.append(pageInfo)
    
def extractFromLinks(links):
    #Obtain each link and extractText from it
    text = list()
    
    #cycle through the links array
    for link in links:
        extractText(link, text)
        
    return text
    