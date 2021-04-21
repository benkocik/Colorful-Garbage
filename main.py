from PIL import Image
import numpy as np
import math
import multiprocessing
import time

CONSTVAL = 17

def getOptimalSize(arrayLength):
    squareSideLen = math.sqrt(arrayLength)
    sideLenDropDec = int(squareSideLen)
    width = math.ceil(arrayLength/sideLenDropDec)
    height = sideLenDropDec
    return (height,width)

def colorMapper(value):
    numvalue = 255
    if value == 'a':
        numvalue = 10*CONSTVAL
    elif value == 'b':
        numvalue = 11*CONSTVAL
    elif value == 'c':
        numvalue = 12*CONSTVAL
    elif value == 'd':
        numvalue = 13*CONSTVAL
    elif value == 'e':
        numvalue = 14*CONSTVAL
    elif value == 'f':
        numvalue = 15*CONSTVAL
    else:
        numvalue = int(value)*CONSTVAL
    
    return numvalue

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=6)
    filePath = input("Enter a file path: ")
    fp = open(filePath, "rb")
    print("Reading file...")
    hexarr = fp.read().hex()
    hexArrLen = len(hexarr)
    print("Calculating optimal size")
    optimalWidth, optimalHeight = getOptimalSize(hexArrLen)
    optimalSize = optimalWidth*optimalHeight
    print("Buffering")
    for i in range(0, optimalSize - hexArrLen):
        hexarr = hexarr + '0'
        
    print("Mapping hex to color")
    mapObj = pool.map(colorMapper, hexarr)
    pool.close()
    pool.join()
    print("Creating numpy array")
    intarr = np.array(list(mapObj))
    print("Reshaping array")
    intarr = intarr.reshape((optimalWidth,optimalHeight))
    i = Image.fromarray(intarr, "RGB")
    i.save('out.bmp')