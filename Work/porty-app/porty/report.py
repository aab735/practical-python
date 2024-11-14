# report.py
#
# Exercise 2.4
import csv
import porty.fileparse as fileparse
from porty.stock import Stock
import porty.tableformat as tableformat
from porty.portfolio import Portfolio

def read_portfolio(filename, **opts):
    with open(filename) as lines:
        return Portfolio.from_csv(lines, **opts)

def read_prices(filename):
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines,types=[str,float],has_headers=False))

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