import csv


i = 1
#  change the path of historical data downloaded .
with open("../CSV/HistoricalQuotes.csv", "r") as source:
    rdr = csv.reader(source)
    with open("../CSV/HistoricalPrices", "w", newline='') as HistoricalPrices:
        wtr = csv.writer(HistoricalPrices)
        for r in rdr:
            if i > 2:
                wtr.writerow((r[0], r[1]))
            i += 1
