# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 21:47:56 2017

@author: USER
"""

import DataScraper
import PriceExtractor
import QuotesScraper
import sys
sys.path.append('../TFIDF/.')
import GenerateMovements
import tfidf


def workflow(companies):
    for company in companies:
        DataScraper.scrape([company])
        QuotesScraper.generate_quotes([company])
        PriceExtractor.getQuoteMovements(company) 
        GenerateMovements.generate_labels(company)
        tfidf.get_tfidf(company)
    
workflow(['aapl','amzn','googl','msft','tsla'])
