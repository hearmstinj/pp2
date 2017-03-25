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
from collections import Counter

global symbol 
symbol = "aapl" 

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
            val = 1 if pred[prev_index - si:x - si].tolist().count(1) >= pred[prev_index - si:x - si].tolist().count(0) else 0
            for y in range(prev_index, x):
                pred[y - si] = val
            prev_index = x
    val = 1 if pred[prev_index - si:x - si].tolist().count(1) >= pred[prev_index - si:x - si].tolist().count(
        0) else 0
    for y in range(prev_index, x):
        pred[y - si] = val
    return pred


def get_accuracies(p, labels, symbol):
    l = ei - p
     
    gnb = GaussianNB()
    y_pred = gnb.fit(V[:p], a[:p]).predict(V[p:])
    print(len(a[p:]), len(y_pred))
    print("Number of mislabelled points out of a total %d points is %d using Gaussian Naive Bayes" % (len(V), (a[p:] != y_pred).sum()))
    y_pred_f = testingpart(p, y_pred, ei, labels)
    naiveaccuracy = (l - (a[p:] != y_pred_f).sum())/l*100
    na_count = (a[p:] != y_pred_f).sum()
    print("Number of mislabelled points out of a total %d points is %d using Gaussian Naive Bayes" % (len(V), (a[p:] != y_pred_f).sum()))

    rnb = RandomForestClassifier(n_estimators=100)
    rfpred = rnb.fit(V[:p], a[:p]).predict(V[p:])
    print("Number of mislabelled points out of a total %d points is %d using Random Forest Classifier" % (len(V), (a[p:] != rfpred).sum()))
    rfpred_f = testingpart(p, rfpred, ei, labels)
    randomaccuracy = (l - (a[p:] != rfpred_f).sum())/l*100
    ra_count = (a[p:] != rfpred_f).sum()
    print("Number of mislabelled points out of a total %d points is %d using Random Forest Classifier" % (len(V), (a[p:] != rfpred_f).sum()))

    ptron = Perceptron(n_iter=50)
    ppred = ptron.fit(V[:p], a[:p]).predict(V[p:])
    print("Number of mislabelled points out of a total %d points is %d using Perceptrons" % (len(V), (a[p:] != ppred).sum()))
    ppred_f = testingpart(p, ppred, ei, labels)
    perceptronaccuracy = (l - (a[p:] != ppred_f).sum())/l*100
    pa_count = (a[p:] != ppred_f).sum()
    print("Number of mislabelled points out of a total %d points is %d using Perceptrons" % (len(V), (a[p:] != ppred_f).sum()))

    svc = SVC()
    spred = svc.fit(V[:p], a[:p]).predict(V[p:])
    print("Number of mislabelled points out of a total %d points is %d using Support Vector Machines" % (len(V), (a[p:] != spred).sum()))
    spred_f = testingpart(p, spred, ei, labels)
    SVMaccuracy = (l - (a[p:] != spred_f).sum())/l*100
    sa_count = (a[p:] != spred_f).sum()
    print("Number of mislabelled points out of a total %d points is %d using Support Vector Machines" % (len(V), (a[p:] != spred_f).sum()))

    dict = {'NaiveBayes' : naiveaccuracy, 'RandomForest': randomaccuracy, 'Perceptron': perceptronaccuracy, 'SVM': SVMaccuracy}

    jsonarray = json.dumps(dict, ensure_ascii=False)
    
    with open('../CSV/FinalResult.csv', 'a') as csvfile:
         writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
         NaiveBayes=[symbol,"GaussianNB",len(V),na_count,naiveaccuracy]
         RFC=[symbol,"RandomForestClassifier",len(V),ra_count,randomaccuracy]
         Perceptrons=[symbol,"Perceptron",len(V),pa_count,perceptronaccuracy]
         svc=[symbol,"SVC",len(V),sa_count,SVMaccuracy]
         writer.writerow(NaiveBayes)
         writer.writerow(RFC)
         writer.writerow(Perceptrons)
         writer.writerow(svc)
          
         
    
    print(jsonarray)

def get_tfidf(company):   
    symbol = company
    labels = generate_tfidf(company)
    get_accuracies(200, labels, company) 
    
    

#get_tfidf('amzn')
