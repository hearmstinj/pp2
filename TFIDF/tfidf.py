import pandas as pd
import sklearn as sk
import random as rd
from sklearn.ensemble import RandomForestClassifier
import csv
from sklearn import feature_extraction
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import Perceptron
from sklearn.svm import SVC
from collections import Counter


def build_df(path):
    df = pd.read_csv(path, header=None, error_bad_lines=False, sep=';')
    #print(df)
    numpy_array = df.as_matrix()
    return numpy_array

data = build_df("../CSV/aapl_information.csv")  # convert data to numpy array
features = data[:, 2:]  # Extract Features/ Training data
labels = data[:, 1:2]  # Extract Labels
# define words to be ignored in a file
'''with open("stop_words.txt") as f:
    words = f.read().split()
f.close()'''

#print(len(features))
#print(labels[0])

#f = ['hey i just met you', 'and this is crazy', 'so heres my number', 'call me maybe', '']
vectorizer = sk.feature_extraction.text.TfidfVectorizer(analyzer='word', min_df=1, stop_words='english')  # tf-idf vectorizer
V = vectorizer.fit_transform(features.ravel()).todense()  # fit the features/ vocab to tf-idf
B = vectorizer.get_feature_names()
doc1 = V[0].tolist()[0]
words_used = [pair for pair in zip(range(0, len(doc1)), doc1) if pair[1] > 0]
#print(words_used)
#print(doc1)
'''print(sorted(words_used, key=lambda t: t[1] * -1))
print(B[5460], B[1946], B[10559])
print(V)
print(len(B))'''

# a = [1 if rd.randint(0, 10) > 3 else 0 for x in range(371)]
# print(a)
atz = list(build_df("../CSV/labels.csv"))
a = atz[0][0].split(',')
# print(a[:271])

gnb = GaussianNB()
y_pred = gnb.fit(V[:271], a[:271]).predict(V[271:])
print("Number of mislabelled points out of a total %d points is %d using Gaussian Naive Bayes" % (len(V), (a[271:] != y_pred).sum()))

rnb = RandomForestClassifier(n_estimators=100)
rfpred = rnb.fit(V[:271], a[:271]).predict(V[271:])
print("Number of mislabelled points out of a total %d points is %d using Random Forest Classifier" % (len(V), (a[271:] != rfpred).sum()))

ptron = Perceptron(n_iter=50)
ppred = ptron.fit(V[:271], a[:271]).predict(V[271:])
print("Number of mislabelled points out of a total %d points is %d using Perceptrons" % (len(V), (a[271:] != ppred).sum()))

svc = SVC()
spred = svc.fit(V[:271], a[:271]).predict(V[271:])
print("Number of mislabelled points out of a total %d points is %d using Support Vector Machines" % (len(V), (a[271:] != spred).sum()))

# trying out some mapping stuff

prev_index = 271
for x in range(271, 371):
    if labels[x][0] != labels[prev_index][0]:
        val = 1 if y_pred[prev_index - 271:x - 271].tolist().count(1) >= y_pred[prev_index - 271:x - 271].tolist().count(0) else 0
        for y in range(prev_index, x):
            y_pred[y - 271] = val
        prev_index = x


