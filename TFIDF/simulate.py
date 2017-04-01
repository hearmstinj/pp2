from zipline.api import order, record, symbol
from zipline import run_algorithm
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import pytz


def initialize(context):
    pass


def handle_data(context, data):
    print(context.portfolio)
    order(symbol('AAPL'), 10)
    record(AAPL=data[symbol('AAPL')].price)


def analyze(context, perf):
    ax1 = plt.subplot(211)
    perf.portfolio_value.plot(ax=ax1)
    ax2 = plt.subplot(212, sharex=ax1)
    perf.AAPL.plot(ax=ax2)
    plt.gcf().set_size_inches(18, 8)
    plt.show()

startDate = datetime(2017, 1, 1, 0, 0, 0, 0, pytz.utc)
endDate = datetime(2017, 3, 29, 0, 0, 0, 0, pytz.utc)

"""data = pd.read_pickle("buyapple_out.pickle")
print(data[:-1])"""
run_algorithm(start=startDate, end=endDate, handle_data=handle_data, initialize=initialize, capital_base=10000.00, analyze=analyze)
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
