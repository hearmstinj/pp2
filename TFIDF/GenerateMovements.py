import pandas as pd

def build(path, separator):
    content = pd.read_csv(path, header=None, sep=separator)
    return content.as_matrix()

quotes_path = "../CSV/QuoteMovements.csv"
articles_path = "../CSV/aapl_information.csv"
movement_data = build(quotes_path, ",")
article_data = build(articles_path, ";")
a = dict()
for row in movement_data:
    a[row[0]] = row[-1]
print(a)
