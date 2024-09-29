# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    f=open(filename,'rt')
    rows = csv.reader(f)
    headers=next(rows)
    total_cost = 0.0
    for line in f:
        row = line.split(',')
        try:
            share_count=float(row[1])
            share_price=float(row[2][:-1])
            total_cost+=share_count*share_price
        except ValueError:
            print('Could not convert string to float')
    f.close()
    #print('Total cost', total_cost)
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:',cost)
