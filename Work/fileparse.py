# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(lines,select=None,types=None,has_headers=True,delimiterVal=',',silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    '''with open(filename) as f:
        if not delimiterVal:
            rows=csv.reader(f)
        else:
            rows=csv.reader(f,delimiter=delimiterVal)'''

    rows = csv.reader(lines,delimiter=delimiterVal)
        
    headers=[]
        
    if has_headers:
        headers=next(rows)

    if select and headers:
        indices=[headers.index(colname) for colname in select]
        headers=select
    else:
        indices=[]

    records=[]
    for rowno,row in enumerate(rows,1):
        if not row:
            continue
            
        if types:
            try:
                row=[func(val) for func,val in zip(types,row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue

        if indices:
            row=[row[index] for index in indices]
            
        if headers:
            record=dict(zip(headers,row))
        else:
            record=tuple(row)
            records.append(record)

    return records
