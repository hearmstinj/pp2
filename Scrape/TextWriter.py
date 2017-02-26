import csv


def writeToCSV(text, symbol):
    fname = "../CSV/" + symbol + "_information.csv"
    with open(fname, "a", encoding='utf-8') as file:
        file.seek(0, 0)
        writer = csv.writer(file, delimiter=';')
        writer.writerows(text)
