from code import randomstring as rs, readfile as rf, readcsv as rc


# Print random line/row from a read file
# Learning about 'as' abreviations

print(rs.randomstring(rf.readfile('data/file0.txt')))
print(rs.randomstring(rc.readcsv('data/file0.csv')))
# remove the newline '\n' from the output
string = rs.randomstring(rf.readfile('data/file0.txt'))
print(string.rstrip())
