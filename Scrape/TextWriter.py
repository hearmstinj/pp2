import csv


def writeToCSV(text, symbol):
    fname = "../CSV/" + symbol + "_information.csv"
    with open(fname, "w", encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(text)
