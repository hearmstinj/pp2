import pandas as pd
import csv


def readfile(path):
    file = pd.read_csv(path, header=0)
    #print(file)
    return file.as_matrix()


def writefile(movements):
    filename = "../CSV/movement.csv"
    with open(filename, "w", encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(movements)

data = readfile("../CSV/HistoricalQuotes.csv")
data = data.tolist()
movement = list()

data = sorted(data)
print(data)
'''for it in range(1, len(data) - 1):
    movement[data[it][0]] = 1 if data[it][2] > data[it + 1][2] else 0'''

print(data[:][0:4])
# writefile(data)


