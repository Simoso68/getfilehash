def readfile(file):
    try:
        return open(file, "rb").read()
    except FileNotFoundError:
        print("error: file not found.")
        exit()