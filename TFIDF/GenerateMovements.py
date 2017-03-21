import pandas as pd
import csv


def build(path, separator):
    content = pd.read_csv(path, header=None, sep=separator)
    return content.as_matrix()


def generate_labels(symbol):
    quotes_path = "../CSV/" + symbol + "_QuoteMovements.csv"
    articles_path = "../CSV/" + symbol + "_information.csv"
    movement_data = build(quotes_path, ",")
    article_data = build(articles_path, ";")
    daily_movements = dict()
    for row in movement_data:
        daily_movements[row[0]] = row[-1]

    labels = list()
    for row in article_data:
        split_values = row[1].split('/')
        day = "0" + split_values[1] if int(split_values[1]) < 10 else split_values[1]
        date = split_values[2] + "/0" + split_values[0] + "/" + day
        label = 1 if date not in daily_movements.keys() else daily_movements[date]
        labels.append(label)

    # print(labels)
    # c = Counter(labels)
    # print(c)
    with open("../CSV/" + symbol + "_labels.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(labels)

generate_labels('aapl')
