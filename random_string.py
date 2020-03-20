from code import randomstring, readfile, readcsv


# Print random line/row from a read file


print(randomstring.randomstring(readfile.readfile('data/file0.txt')))
print(randomstring.randomstring(readcsv.readcsv('data/file0.csv')))
# remove the newline '\n' from the output
string = randomstring.randomstring(readfile.readfile('data/file0.txt'))
print(string.rstrip())
