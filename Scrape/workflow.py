# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 21:47:56 2017

@author: USER
"""

from DataScraper import scrape
import PriceExtractor
import sys
sys.path.append('../TFIDF/.')
import GenerateMovements
import tfidf


def workflow(company):
    DataScraper.scrape(company)
    # PriceExtractor.getQuoteMovements(company)
    GenerateMovements.generate_labels(company)
    tfidf.get_tfidf(company)
    
workflow('aapl')
