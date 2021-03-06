from cryptoUtils import encrypt
from cryptoUtils import decrypt
import numpy as np
from hashlib import sha256
def getHexFromFile(pathToFile : str) -> str:
    fp = open(pathToFile, 'rb')
    someBytes = fp.read()
    hexStr = someBytes.hex()
    fp.close()
    return hexStr

def getEncryptedHexFromFile(pathToFile : str, key : bytes) -> str:
    fp = open(pathToFile, 'rb')
    fileAsBytes = fp.read()
    fp.close()
    return encrypt(fileAsBytes, key).hex()

def writeHexString(pathToNewFile : str, dataToWrite : str):
    fileAsBytes = bytes.fromhex(dataToWrite)
    fp = open(pathToNewFile, 'wb')
    fp.write(fileAsBytes)
    fp.close()

def writeEncryptedHexString(pathToNewFile : str, dataToWrite : str, key : bytes):
    data = decrypt(bytes.fromhex(dataToWrite), key)
    fp = open(pathToNewFile, 'wb')
    fp.write(data.decode())
    fp.close()

def stringToBinary(m):
    if type(m) == str:
        return ''.join([ format(ord(i), "08b") for i in m ])
    elif type(m) == bytes or type(m) == np.ndarray:
        return [ format(i, "08b") for i in m ]
    elif type(m) == int or type(m) == np.uint8:
        return format(m, "08b")
    else:
        raise TypeError("Input type not supported")