import csv
i=1
#change the path of historucal data downloaded .
with open("HistoricalQuotes.csv","r") as source:
    rdr= csv.reader( source )
    with open("HistoricalPrices","w", newline='') as HistoricalPrices:
        wtr= csv.writer(HistoricalPrices)
        for r in rdr:
            if i > 2:
                wtr.writerow( (r[0], r[1]) )
            i=i+1;
