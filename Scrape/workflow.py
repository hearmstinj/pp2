# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 21:47:56 2017

@author: USER
"""

import DataScrapper
import PriceExtractor
import GenerateMovements
import tfidf

def workflow(company):
    DataScrapper.scrape(['aapl'])
    PriceExtractor.getQuoteMovements('aapl')
    GenerateMovements.getMovement('aapl')
    tfidf.get_tfidf('aapl')
    
workflow('aapl')    