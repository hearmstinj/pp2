# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 21:47:56 2017

@author: USER
"""

import DataScraper
import PriceExtractor
import sys
sys.path.append('../TFIDF/GenerateMovements')
sys.path.append('../TFIDF/tfidf')
import GenerateMovements
import tfidf

def workflow(company):
    DataScraper.scrape(['aapl'])
    PriceExtractor.getQuoteMovements('aapl')
    GenerateMovements.getMovement('aapl')
    tfidf.get_tfidf('aapl')
    
workflow('aapl')    