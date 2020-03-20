from code import readfile, readcsv


# Documentation - https://docs.python.org/3.7/library/importlib.html
# Based on https://stackoverflow.com/a/20749411/8949196, https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder/20753073#20753073
# Atom + pyflakes doesnt like * will have to define them manually; but python doesnt complain.

print(readfile.readfile('data/file0.txt'))
print(readcsv.readcsv('data/file0.csv'))
