import csv


def writeToCSV(text, symbol):
    fname = "../CSV/" + symbol + "_information.csv"
    with open(fname, "r+", encoding='utf-8') as file:
        old = file.read()
        file.seek(0)
        writer = csv.writer(file, delimiter=';')
        writer.writerows(text)
        file.write(old)
