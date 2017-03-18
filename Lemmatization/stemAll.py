from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import pandas as pd
import csv


def build_df(path):
    df = pd.read_csv(path, header=None, error_bad_lines=False, sep=';')
    numpy_array = df.as_matrix()
    return numpy_array


def stem(symbols):
    for symbol in symbols:
        data = build_df("../CSV/" + symbol + "_information.csv")  # convert data to numpy array
        pts = PorterStemmer()

        # Go through each text portion of the data-frame and stem the article
        for datum in data:
            print(datum[2])
            temp_text = datum[2]
            datum[2] = " ".join([pts.stem(i) for i in temp_text.split()])
            print(datum[2])

        with open("../CSV/" + symbol + "_information_stemmed.csv", "w", encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(data)

stem(['aapl', 'amzn', 'csco', 'tsla', 'ssnlf', 'msft', 'googl'])