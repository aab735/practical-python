# report.py
#
# Exercise 2.4
import csv
import fileparse
import stock
import tableformat

def read_portfolio(filename):
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,select=['name','shares','price'],types=[str,int,float])
    return [stock.Stock(d['name'],d['shares'],d['price']) for d in portdicts]

    '''portfolio = []

    with open(filename, 'rt') as f:
        rows=csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers,row))
            stock = {'name':record['name'],'shares':int(record['shares']),'price':float(record['price'])}
            portfolio.append(stock)
    return portfolio'''

def read_prices(filename):
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines,types=[str,float],has_headers=False))

    '''stock_price = {}

    with open(filename, 'rt') as f:
        rows=csv.reader(f)
        for row in rows:
            try:
                stock_price[row[0]]=float(row[1])
            except IndexError:
                pass
    return stock_price'''

def gain_or_loss():
    cost_value=0.0
    total_value=0.0

    portfolio = read_portfolio('Data/portfolio.csv')
    stock_price = read_prices('Data/prices.csv')

    for row in portfolio:
        cost_value+=row['shares']*row['price']
        total_value+=row['shares']*stock_price[row['name']]
    
    return total_value - cost_value

def make_report(portfolioList,priceDict):
    report = []
    for row in portfolioList:
        profit_or_loss = priceDict[row.name] - float(row.price)
        report.append((row.name,row.shares,priceDict[row.name],profit_or_loss))
    return report

def print_report(reportdata,formatter):
    '''headers=('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' %headers)
    print(('-'*10+' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)'''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name,shares,price,change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_filename,prices_filename,fmt='txt'):
    portfolio = read_portfolio(portfolio_filename)
    stock_price = read_prices(prices_filename)
    report=make_report(portfolio,stock_price)
    formatter = tableformat.create_formatter(fmt)
    print_report(report,formatter)


def main(args):
    if len(args)!=4:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1],args[2],args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)