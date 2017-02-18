# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 18:45:30 2017

@author: USER
"""
import csv
prev=0
i=0
with open("../CSV/HistoricalQuotes.csv", 'r') as csvfile:
     with open("../CSV/HistoricalQuotes1.csv", 'w')  as output:
         reader = csv.reader(csvfile, delimiter=',')
         writer = csv.writer(output)
         for row in reader:
             if i > 0:
                 current=float(row[1])
                 movement=prev-current
                 prev=current
                 if movement > 0:
                     writer.writerow(row + [1])
                 else:
                     writer.writerow(row + [0])
             i=i+1
 #   movement[data[it][0]] = 1 if data[it][2] > data[it + 1][2] else 0
#
#writefile(movement)
        
    