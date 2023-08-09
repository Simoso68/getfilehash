import hashlib

def getsha1(input):
    hash = hashlib.sha1()
    hash.update(input)
    hash.digest()
    return hash.hexdigest()
def getsha256(input):
    hash = hashlib.sha256()
    hash.update(input)
    hash.digest()
    return hash.hexdigest()
def getsha512(input):
    hash = hashlib.sha512()
    hash.update(input)
    hash.digest()
    return hash.hexdigest()
def getmd5(input):
    hash = hashlib.md5()
    hash.update(input)
    hash.digest()
    return hash.hexdigest()