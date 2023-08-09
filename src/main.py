from sys import argv
from read import readfile
from hash import *

VERSION = "1.0.0"
print_version = False
print_help = False
files = []

if argv[1] == "sha1" or argv[1] == "sha256" or argv[1] == "sha512" or argv[1] == "md5":
    hashtype = argv[1]
else:
    print(f"error: unknown hashing algorithm: {argv[1]}")
    exit()

for arg in argv[2:]:
    if arg.startswith("-"):
        if arg == "-v" or arg == "--version":
            print_version = True
        elif arg == "-h" or arg == "--help":
            print_help = True
        else:
            print(f"error: unknown argument: {arg}")
            exit()
    else:
        files.append(arg)

for file in files:
    if hashtype == "sha1": print(getsha1(readfile(file)))
    elif hashtype == "sha256": print(getsha256(readfile(file)))
    elif hashtype == "sha512": print(getsha512(readfile(file)))
    elif hashtype == "md5": print(getmd5(readfile(file)))

if print_version:
    print(f"getfilehash by Simoso68 running on version {VERSION}, licensed under GNU GPL 3.")
if print_help:
    print("""
General usage:
    <hash-algorithm> <files>
Arguments:
    -v / --version              Output version of getfilehash
    -h / --help                 Help for getfilehash
Example:
    sha256 file1.o file2.o""".replace("\n", "", 1))