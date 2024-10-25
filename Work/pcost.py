# pcost.py
#
# Exercise 1.27
import sys
import csv
import report

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return sum([s.shares*s.price for s in portfolio])
    
'''
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
    '''

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    cost = portfolio_cost(args[1])
    print ('Total cost:',cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)

'''if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv

cost = portfolio_cost(filename)
print('Total cost:',cost)'''
