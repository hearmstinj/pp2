import LinkExtractor
import TextExtractor
import TextWriter

def scrape(symbols):
    for symbol in symbols:
        baseURL = "http://nasdaq.com/symbol/" + symbol + "/news-headlines"
        nodeURL = baseURL + "?page="
        
        #call function to scrape all internal links and return a list
        links = LinkExtractor.extract(baseURL, nodeURL, symbol)
        print("Finished loading " + symbol + " links")

        #call function to go to each link and extract data
        text = TextExtractor.extractFromLinks(links)
        print("Finished loading text.")
        
        #write the csv data to file
        TextWriter.writeToCSV(text, symbol)
        print("Finished writing file.")           