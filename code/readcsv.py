import csv


# Documentation
# https://docs.python.org/3.7/library/csv.html


def readcsv():
    '''Read file, return the content as a list'''
    file = 'data/file0.csv'
    with open(file, newline='') as data:
        data = csv.reader(data, delimiter=',', quotechar='|')
        rowofdata = []
        for row in data:
            rowofdata.append(row)
    return rowofdata


# print(readcsv())   # expected output [['file0,line0'], ['file0,line1'], ['file0,line2'], ['file0,line3'], ['file0,line4'], ['file0,line5']]
