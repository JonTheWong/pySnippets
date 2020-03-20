from code import readfile, readcsv
# Based on https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder/20753073#20753073
# Atom + pyflakes doesnt like * will have to define them manually; but python doesnt complain.

print(readfile.readfile())
print(readcsv.readcsv())
