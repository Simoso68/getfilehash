def readfile(file):
    try:
        return open(file, "rb").read()
    except FileNotFoundError:
        print("error: file not found.")
        exit(1)
    except OSError as x:
        print(f"error: operating system related error: {x})
        exit(1)
