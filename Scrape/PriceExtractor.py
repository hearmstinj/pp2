import csv

def getQuoteMovements(company):
    prev = 0
    with open('../CSV/' + company + '_HistoricalQuotes.csv', 'r') as csvfile:
        with open('../CSV/'+ company + '_QuoteMovements.csv', 'w') as output:
            reader = csv.reader(csvfile, delimiter=',')
            writer = csv.writer(output)
            for row in reversed(list(reader)):
                current = float(row[1])
                movement = current-prev
                prev = current
                if movement > 0:
                    writer.writerow(row + [1])
                else:
                    writer.writerow(row + [0])
                    