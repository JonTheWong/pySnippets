import csv


# Documentation
# https://docs.python.org/3.7/library/csv.html
# csv.reader already splits the list data so daae[0] works out of the box.


def readcsv(filepath):
    '''
    Read file in filepath, return all rows as a list type.
    Call function: ```readcsv('data/file0.csv')```
    '''
    with open(filepath, newline='', encoding='utf-8') as data:
        data = csv.reader(data, delimiter=',', quotechar='|')
        rowofdata = []
        for row in data:
            rowofdata.append(row)
    return rowofdata


# print(readcsv('data/file0.csv'))   # expected output [['file0,line0'], ['file0,line1'], ['file0,line2'], ['file0,line3'], ['file0,line4'], ['file0,line5']]
