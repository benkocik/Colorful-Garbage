'''
Programmers: Kyle Heestand and Ben Kocik
Description: Handles all steganography. Takes dictionary as input from main.py
'''

# Imports
from reference import messageToBinary
import cv2
import numpy as np
import logging

def encode_text(image, message):
    '''
    Encodes specified message into provided image

            Parameters:
                image: string file path of image that will have data encoded to it
                message: string of text to encode into image

            Returns:
                CV2 image with hidden message - convert with imwrite
    '''
    im = cv2.imread(image)  # Read image
    n_bytes = im.shape[0] * im.shape[1] * 3 // 8    # Calculate max bytes
    message += "#####"  # Use 5 '#'s to signify end of message - this is standard for encoding and decoding
    # Check message can fit into image
    if len(message) > n_bytes:
        logging.error("Message is too large or image is too small. The data will not fit into the image. Try a smaller message or larger image")
        raise ValueError("Message too large or image too small, need bigger image or less data")

    i = 0
    bin_message = messageToBinary(message)  # Convert data to binary

    # Break image into values
    for values in im:
        # Break values into pixels
        for pixel in values:
            # Convert rgb of pixel into binary
            r, g, b = messageToBinary(pixel)
            # RED IN PIXEL
            if i < len(bin_message):
                # Hide data into LSB
                pixel[0] = int(r[:-1] + bin_message[i], 2)
                i += 1
            # GREEN IN PIXEL
            if i < len(bin_message):
                # Hide data into LSB
                pixel[1] = int(g[:-1] + bin_message[i], 2)
                i+= 1
            # BLUE IN PIXEL
            if i < len(bin_message):
                # Hide data into LSB
                pixel[2] = int(b[:-1] + bin_message[i], 2)
                i+=1
            # Data is fully encoded, leave for loop
            if i >= len(bin_message):
                break

    return im


def encode_file():
    '''
    
    '''
    # TODO Encode file into image

def decode_text():
    '''

    '''

def decode_file():
    '''
    
    '''


def Steganography(argDict):
    '''
    Assigns inputs to variables. Begins steganography.

            Parameters:
                argDict: dictionary of arguments provided

            Returns:
                Output file or revealed message
    '''
    # Get values from argDict
    startImage = argDict['input']   # Image inputted
    message = argDict['message']    # Message to hide TODO Check if empty
    file_to_hide = argDict['file_to_hide'] # TODO Figure out what file_to_hide is and do check if empty
    process = argDict['process']    # TODO Figure out what this is...
    outFile = argDict['out']        # Image file to output to TODO may need to check if empty

    # Check data to determine what to do
    if message != None:
        # Hide message in image
        logging.debug("Mode: Hiding text into image")
        encodedImage = encode_text(startImage, message)
        cv2.imwrite(outFile, encodedImage)

    elif file_to_hide != None:
        logging.debug("Mode: Hiding file into image")
        encode_file(startImage, file_to_hide)

    elif message == None and file_to_hide == None:
        logging.debug("Mode: Unhiding message/file from image")
        # TODO decide on how to handle text and file decoding
        decodedText = decode_text()
        decode_file()

