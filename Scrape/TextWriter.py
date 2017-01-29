import csv

def writeToCSV(text, symbol):
    fname = symbol + "_information.csv"
    with open(fname, "w") as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerows(text)