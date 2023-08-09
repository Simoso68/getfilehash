contents = "#!/bin/python3\n\n" + open("src/read.py").read() + "\n\n" + open("src/hash.py").read() + "\n\n" + open("src/main.py").read()
contents = contents.replace("from read import readfile", "", 1).replace("from hash import *", "", 1)

file = open("getfilehash", "w")
file.write(contents)
file.close()