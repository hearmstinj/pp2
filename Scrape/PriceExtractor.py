import csv


prev = 0
i = 0
with open('../CSV/HistoricalQuotes.csv', 'r') as csvfile:
    with open('../CSV/HistoricalQuotes.csv', 'w') as output:
        reader = csv.reader(csvfile, delimiter=',')
        writer = csv.writer(output)
        for row in reader:
            if i > 0:
                current = float(row[1])
                movement = current-prev
                prev = current
                if movement > 0:
                    writer.writerow(row + [1])
                else:
                    writer.writerow(row + [0])
            i += 1
