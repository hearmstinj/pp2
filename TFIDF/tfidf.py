import pandas as pd
import sklearn as sk
import random as rd
from sklearn.ensemble import RandomForestClassifier
import csv
import json
from sklearn import feature_extraction
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import Perceptron
from sklearn.svm import SVC
from collections import OrderedDict
import numpy as np

global symbol 
symbol = "aapl" 


def convert_date(string_date):
    values = string_date.split('/')
    date = values[2] + "-" + values[0] + "-" + values[1]
    return date


def build_df(path):
    df = pd.read_csv(path, header=None, error_bad_lines=False, sep=';')
    #print(df)
    numpy_array = df.as_matrix()
    return numpy_array


def generate_tfidf(company):
    data1 = build_df("../CSV/" + company + "_information.csv")  # convert data to numpy array
    data = data1[::-1, :]
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
    global V
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

           # IMPORTANT MUST READ
           # FIRST RUN DATASCRAPER.PY -> RUN PRICE EXTRACTOR.PY -> RUN GENERATEMOVEMENTS.PY -> RUN TFIDF.PY
    atz = list(build_df("../CSV/" + company + "_labels.csv"))
    a1 = atz[0][0].split(',')
    global a
    a = a1[::-1]
    global ei
    ei = len(V)
    return labels


def testingpart(si, pred, ei, labels):
    prev_index = si
    for x in range(si, ei):
        if labels[x][0] != labels[prev_index][0]:
            # print(pred[prev_index - si:x - si].tolist().count('1'))
            # print(pred[prev_index - si:x - si].tolist().count('0'))
            val = 1 if pred[prev_index - si:x - si].tolist().count('1') > pred[prev_index - si:x - si].tolist().count('0') else 0
            for y in range(prev_index, x):
                pred[y - si] = val
            prev_index = x
    val = 1 if pred[prev_index - si:x - si].tolist().count(1) > pred[prev_index - si:x - si].tolist().count(
        0) else 0
    for y in range(prev_index, x):
        pred[y - si] = val
    return pred


def get_accuracies(p, labels, symbol):
    l = ei - p
     
    gnb = GaussianNB()
    y_pred = gnb.fit(V[:p], a[:p]).predict(V[p:])
    print(len(a[p:]), len(y_pred), len(V[p:]), len(V[:p]))
    print("Number of mislabelled points out of a total %d points is %d using Gaussian Naive Bayes" % (len(V), (a[p:] != y_pred).sum()))
    y_pred_f = testingpart(p, y_pred, ei, labels)
    naiveaccuracy = (l - (a[p:] != y_pred).sum())/l*100
    na_count = (a[p:] != y_pred_f).sum()
    print("Number of mislabelled points out of a total %d points is %d using Gaussian Naive Bayes" % (len(V), (a[p:] != y_pred_f).sum()))

    rnb = RandomForestClassifier(n_estimators=100)
    rfpred = rnb.fit(V[:p], a[:p]).predict(V[p:])
    print("Number of mislabelled points out of a total %d points is %d using Random Forest Classifier" % (len(V), (a[p:] != rfpred).sum()))
    temp_pred = np.copy(rfpred)
    rfpred_f = testingpart(p, rfpred, ei, labels)
    # for x in range(p, len(V)):
        # print([labels[x][0], temp_pred[x - p], rfpred_f[x - p]])

    randomaccuracy = (l - (a[p:] != rfpred).sum())/l*100
    ra_count = (a[p:] != rfpred_f).sum()
    print("Number of mislabelled points out of a total %d points is %d using Random Forest Classifier" % (len(V), (a[p:] != rfpred_f).sum()))

    ptron = Perceptron(n_iter=50)
    ppred = ptron.fit(V[:p], a[:p]).predict(V[p:])
    print("Number of mislabelled points out of a total %d points is %d using Perceptrons" % (len(V), (a[p:] != ppred).sum()))
    ppred_f = testingpart(p, ppred, ei, labels)
    perceptronaccuracy = (l - (a[p:] != ppred).sum())/l*100
    pa_count = (a[p:] != ppred_f).sum()
    print("Number of mislabelled points out of a total %d points is %d using Perceptrons" % (len(V), (a[p:] != ppred_f).sum()))

    svc = SVC()
    spred = svc.fit(V[:p], a[:p]).predict(V[p:])
    print("Number of mislabelled points out of a total %d points is %d using Support Vector Machines" % (len(V), (a[p:] != spred).sum()))
    spred_f = testingpart(p, spred, ei, labels)
    SVMaccuracy = (l - (a[p:] != spred).sum())/l*100
    sa_count = (a[p:] != spred_f).sum()
    print("Number of mislabelled points out of a total %d points is %d using Support Vector Machines" % (len(V), (a[p:] != spred_f).sum()))

    # Testing out different SVM kernels over here
    lsvm = SVC(kernel='linear')
    lsvmpred = lsvm.fit(V[:p], a[:p]).predict(V[p:])
    print("Number of mislabelled points out of a total %d points is %d using LinearSVM" % (
        len(V), (a[p:] != lsvmpred).sum()))
    lsvmpred_f = testingpart(p, lsvmpred, ei, labels)
    LSVMaccuracy = (l - (a[p:] != lsvmpred).sum()) / l * 100
    lsvma_count = (a[p:] != lsvmpred_f).sum()
    print("Number of mislabelled points out of a total %d points is %d using LinearSVM" % (
        len(V), (a[p:] != lsvmpred_f).sum()))

    rsvm = SVC(kernel='rbf', gamma=100)
    rsvmpred = rsvm.fit(V[:p], a[:p]).predict(V[p:])
    print("Number of mislabelled points out of a total %d points is %d using RBFKernel" % (
        len(V), (a[p:] != rsvmpred).sum()))
    rsvmpred_f = testingpart(p, rsvmpred, ei, labels)
    RSVMaccuracy = (l - (a[p:] != rsvmpred).sum()) / l * 100
    rsvma_count = (a[p:] != rsvmpred_f).sum()
    print("Number of mislabelled points out of a total %d points is %d using RBFKernel" % (
        len(V), (a[p:] != rsvmpred_f).sum()))
    # END TESTING OUT DIFFERENT SVM
    dict = {'NaiveBayes' : naiveaccuracy, 'RandomForest': randomaccuracy, 'Perceptron': perceptronaccuracy, 'SVM': SVMaccuracy, 'LSVM': LSVMaccuracy, 'RSVM': RSVMaccuracy}

    jsonarray = json.dumps(dict, ensure_ascii=False)
    
    with open('../CSV/FinalResult.csv', 'a') as csvfile:
         writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
         NaiveBayes=[symbol, "GaussianNB", naiveaccuracy]
         RFC=[symbol, "RandomForestClassifier", randomaccuracy]
         Perceptrons=[symbol, "Perceptron", perceptronaccuracy]
         svc=[symbol, "SVC", SVMaccuracy]
         """
         writer.writerow(NaiveBayes)
         writer.writerow(RFC)
         writer.writerow(Perceptrons)
         """
         writer.writerow(svc)

    print(jsonarray)

    # Save to JSON format
    day_predictions_dict = OrderedDict()
    for x in range(p, ei):
        day_predictions_dict[convert_date(labels[x][0])] = spred_f[x - p]
    write_predictions(symbol, day_predictions_dict)


def write_predictions(company, predictions):
    with open("../CSV/" + company + "_predictions.json", "w") as file:
        json.dump(predictions, file)


def get_tfidf(company):   
    symbol = company
    labels = generate_tfidf(company)
    get_accuracies(400, labels, company)
    
    

#get_tfidf('amzn')
