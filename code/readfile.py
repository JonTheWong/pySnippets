import glob


# Documentation
# https://docs.python.org/3.7/library/glob.html


def readFile():
    '''Read file(s), return all lines as a list'''
    file = '../data/file0.txt'
    for line in glob.iglob(file, recursive=True):
        with open(line) as data:
            data = data.readlines()
        return data


print(readFile())   # expected output ['file0,line0\n', 'file0,line1\n']
