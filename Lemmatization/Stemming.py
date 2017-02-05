from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
import nltk
import string
import os
import pandas as pd

import csv

stemmer = PorterStemmer()


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems


def build_df(path):
    df = pd.read_csv(path, header=None, error_bad_lines=False, sep=';')
    numpy_array = df.as_matrix()
    return numpy_array


data = build_df("../TFIDF/aapl_information.csv")
features = data[:, 2:]
lowers = features.lower()
no_punctuation = lowers.translate(None, string.punctuation)

tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(no_punctuation)
print(tfs)