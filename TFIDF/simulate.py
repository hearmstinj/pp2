from zipline.api import order, record, symbol
from zipline import run_algorithm
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import pytz


def initialize(context):
    pass


def handle_data(context, data):
    order(symbol('AAPL'), 10)
    record(AAPL=data[symbol('AAPL')].price)


def analyze(context, perf):
    ax1 = plt.subplot(211)
    perf.portfolio_value.plot(ax=ax1)
    ax2 = plt.subplot(212, sharex=ax1)
    perf.capital_used.plot(ax=ax2)
    plt.gcf().set_size_inches(18, 8)
    plt.show()

startDate = datetime(2017, 1, 1, 0, 0, 0, 0, pytz.utc)
endDate = datetime(2017, 3, 25, 0, 0, 0, 0, pytz.utc)

data = pd.read_pickle("buyapple_out.pickle")
for x in data:
    print(x)
run_algorithm(start=startDate, end=endDate, initialize=initialize, capital_base=10000.00, analyze=analyze)
