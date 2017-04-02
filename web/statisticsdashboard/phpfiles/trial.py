
from zipline.api import order, record, symbol
from zipline import run_algorithm
import pandas as pd
from datetime import datetime
import pytz
import json
from collections import OrderedDict
from datetime import datetime
import matplotlib.pyplot as plt, mpld3
import sys


pred = 1
count = 0

def initialize(context):
    pass


def handle_data(context, data):
    global count
    if pred == 1:
        count += 1
    else:
        count = 0
    if context.portfolio.cash > 0:
        order(symbol('AAPL'), (count + 1) * 10)
    else:
        order(symbol('AAPL'), -10 * count)
        count = 0
    record(AAPL=data[symbol('AAPL')].price)
    print(context.portfolio)


def analyze(context, perf):
    fig = plt.figure()
    ax1 = plt.subplot(211)
    perf.portfolio_value.plot(ax=ax1)
    ax2 = plt.subplot(212, sharex=ax1)
    perf.AAPL.plot(ax=ax2)
    plt.gcf().set_size_inches(18, 8)
    html = mpld3.fig_to_html(fig, no_extras=False, template_type="simple")
    # print(html)
    text = html.split(' ')
    furnished_text = ' '.join(text)
    # print(len(furnished_text))
    # return furnished_text
    assoc_data = str(perf.starting_cash[0]) + " " +  str(perf.ending_cash[-1]) + " " +  str(perf.algorithm_period_return[-1])

    with open("graph.txt", "w") as file:
        file.write(html)

    with open("associated_data.txt", "w") as file:
        file.write(assoc_data)
    print(assoc_data)
    # plt.show()

start_args = sys.argv[1].split('/')
end_args = sys.argv[2].split('/')
capital = sys.argv[3]
startDate = datetime(int(start_args[0]), int(start_args[1]), int(start_args[2]), 0, 0, 0, 0, pytz.utc)
endDate = datetime(int(end_args[0]), int(end_args[1]), int(end_args[2]), 0, 0, 0, 0, pytz.utc)

"""data = pd.read_pickle("buyapple_out.pickle")
print(data[:-1])"""
run_algorithm(start=startDate, end=endDate, handle_data=handle_data, initialize=initialize, capital_base=float(capital), analyze=analyze)


"""
# The format of the Portfolio variable under context
Portfolio(
    {
        'positions_value': 1160.2,
        'starting_cash': 10000.0,
        'capital_used': -1161.200000000026,
        'cash': 8838.799999999974,
        'start_date': Timestamp('2017-01-03 00:00:00+0000', tz='UTC', offset='C'),
        'returns': -0.00010000000000254658,
        'positions': {
            Equity(
                0,
                symbol='AAPL',
                asset_name='Apple Inc',
                exchange='QUANDL',
                start_date=Timestamp('1980-12-12 00:00:00+0000', tz='UTC'),
                end_date=Timestamp('2017-03-28 00:00:00+0000', tz='UTC'),
                first_traded=None,
                auto_close_date=Timestamp('2017-03-29 00:00:00+0000', tz='UTC'),
                exchange_full='QUANDL'): Position({
                'sid': Equity(
                    0,
                    symbol='AAPL',
                    asset_name='Apple Inc',
                    exchange='QUANDL',
                    start_date=Timestamp('1980-12-12 00:00:00+0000', tz='UTC'),
                    end_date=Timestamp('2017-03-28 00:00:00+0000', tz='UTC'),
                    first_traded=None,
                    auto_close_date=Timestamp('2017-03-29 00:00:00+0000', tz='UTC'),
                    exchange_full='QUANDL'),
                'amount': 10,
                'last_sale_price': 116.02,
                'last_sale_date': Timestamp('2017-01-04 21:00:00+0000', tz='UTC'),
                'cost_basis': 116.12000000000259})
        },
        'portfolio_value': 9998.9999999999745,
        'positions_exposure': 1160.2,
        'pnl': -1.0000000000254659
    }
)
"""
