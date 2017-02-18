import pandas as pd
import csv
from collections import Counter

def build(path, separator):
    content = pd.read_csv(path, header=None, sep=separator)
    return content.as_matrix()

quotes_path = "../CSV/QuoteMovements.csv"
articles_path = "../CSV/aapl_information.csv"
movement_data = build(quotes_path, ",")
article_data = build(articles_path, ";")
daily_movements = dict()
for row in movement_data:
    daily_movements[row[0]] = row[-1]

# print(a)
labels = list()
for row in article_data:
    split_values = row[1].split('/')
    date = split_values[2] + "/0" + split_values[0] + "/" + split_values[1]
    label = 1 if date not in daily_movements.keys() else daily_movements[date]
    labels.append(label)

# print(labels)
# c = Counter(labels)
# print(c)
with open("../CSV/labels.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(labels)
