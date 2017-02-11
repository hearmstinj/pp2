import csv


def writeToCSV(text, symbol):
    fname = symbol + "_information.csv"
    with open(fname, "w", encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(text)
    with open(fname, "w", 'utf-8') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerows(text)

