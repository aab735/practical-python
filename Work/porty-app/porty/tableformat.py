class TableFormatter:
    def headings(self,headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()
    
    def row(self,rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self,headers):
        for h in headers:
            print(f'{h:>10s}',end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))
    
    def row(self,rowdata):
        for d in rowdata:
            print(f'{d:>10s}',end=' ')
        print()
    
class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML Format
    '''
    def headings(self,headers):
        print('<tr><th>'+'</th><th>'.join(headers)+'</th></tr>')
    
    def row(self,rowdata):
        print('<tr><td>'+'</td><td>'.join(rowdata)+'</td></tr>')


class CSVTableFormatter(TableFormatter):
    '''
    Output protfolio data in CSV format
    '''
    def headings(self,headers):
        print(','.join(headers))
    
    def row(self,rowdata):
        print(','.join(rowdata))

class FormatError(Exception):
    pass

def create_formatter(name):
    if name=='txt':
        return TextTableFormatter()
    elif name=='csv':
        return CSVTableFormatter()
    elif name=='html':
        return HTMLTableFormatter()
    else:
        #raise RecursionError(f'Unknown format {name}')
        raise FormatError('Unknown table format %s' %name)
    
def print_table(objects,columns,formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [str(getattr(obj,name)) for name in columns]
        formatter.row(rowdata)