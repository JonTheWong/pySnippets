import glob


# Documentation
# https://docs.python.org/3.7/library/glob.html

def readfile(filepath):
    '''
    Read file in filepath, return all lines as a list type.
    Call function: ```readfile('data/file0.txt')```
    '''
    for line in glob.iglob(filepath, recursive=True):
        with open(line) as data:
            data = data.readlines()
        return data


# print(readfile())   # expected output ['file0,line0\n', 'file0,line1\n']
