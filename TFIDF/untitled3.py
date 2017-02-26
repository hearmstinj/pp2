# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 19:29:43 2017

@author: USER
"""

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
print (data[0])

movement = []

print(data[0])
for it in range(1, len(data) - 1):
    if data[it][2] > data[it + 1][2]:
        movement.append(1)
    else:
        movement.append(0)    

writefile(movement)