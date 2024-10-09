# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers=next(rows)
        total_cost = 0.0
        for lineno, line in enumerate(rows,start=1):
            record = dict(zip(headers,line))
            try:
                share_count=int(record['shares'])
                share_price=float(record['price'])
                total_cost+=share_count*share_price
            except ValueError:
                print(f'Row {lineno}: Couldn\'t convert: {line}')
    #print('Total cost', total_cost)
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total cost:',cost)
