'''
Programmers: Kyle Heestand and Ben Kocik
Description: Handles all steganography. Takes dictionary as input from main.py
'''

# Imports
import cv2
import logging
import sys
from utils import stringToBinary

# Constants for end of message types
# Use 5 '#'s to signify end of string type message
STRING_END = "#####"
# Use 5 '$'s to signify end of file type message
FILE_END = "$$$$$"

def encode_text(image, message, messageType):
    '''
    Encodes specified message into provided image

            Parameters:
                image: string file path of image that will have data encoded to it
                message: string of text to encode into image
                messageType: boolean to determine string or file. True for string, False for file

            Returns:
                im: CV2 image with hidden message - convert with imwrite
    '''
    im = cv2.imread(image)  # Read image
    nBytes = im.shape[0] * im.shape[1] * 3 // 8    # Calculate max bytes
    # Based on message type, add string to end
    if messageType:
        message += STRING_END
    elif not messageType:
        message += FILE_END
    # Check message can fit into image
    if len(message) > nBytes:
        logging.error("Message is too large or image is too small. The data will not fit into the image. Try a smaller message or larger image")
        sys.exit(1)

    i = 0
    binaryMessage = stringToBinary(message)  # Convert data to binary

    # Break image into values
    for values in im:
        # Break values into pixels
        for pixel in values:
            # Convert rgb of pixel into binary
            r, g, b = stringToBinary(pixel)
            # RED IN PIXEL
            if i < len(binaryMessage):
                # Hide data into LSB
                pixel[0] = int(r[:-1] + binaryMessage[i], 2)
                i += 1
            # GREEN IN PIXEL
            if i < len(binaryMessage):
                # Hide data into LSB
                pixel[1] = int(g[:-1] + binaryMessage[i], 2)
                i+= 1
            # BLUE IN PIXEL
            if i < len(binaryMessage):
                # Hide data into LSB
                pixel[2] = int(b[:-1] + binaryMessage[i], 2)
                i+=1
            # Data is fully encoded, leave for loop
            if i >= len(binaryMessage):
                break
    
    return im   # Return cv2 image 

def decode_text(image):
    '''
    Decodes message from specified image file

            Parameters:
                image: string file path of image that will have data encoded to it

            Returns:
                message: string message that was decoded from image
                messageType: boolean message type. True for string, False for file
    '''
    im = cv2.imread(image)  # Read image
    binaryData = ""
    # Break image into values
    for values in im:
        # Break values into pixels
        for pixel in values:
            # Convert rgb of pixel into binary
            r, g, b = stringToBinary(pixel)
            binaryData += r[-1] # Get LSB from red
            binaryData += g[-1] # Get LSB from green
            binaryData += b[-1] # Get LSB from blue
    # Split into 8 bits - 8 bits in a byte
    byteData = [binaryData[i: i+8] for i in range(0, len(binaryData), 8)]
    message = ""
    for byte in byteData:
        message += chr(int(byte, 2))
        # Check if string or file
        if message[-5:] == STRING_END:
            messageType = True
            break
        elif message[-5:] == FILE_END:
            messageType = False
            break
        else:
            logging.error("Message not found in image, try a different image")
            sys.exit(1)

    if message[:-5] == STRING_END or message[:-5] == FILE_END:
        message = message[:-5]  # Remove ending from message
    else:
        logging.error("Message not found in image, try a different image")
        sys.exit(1)

    return message, messageType     # Return message as string and message type as boolean
    

def steganography(argDict, mode):
    '''
    Assigns inputs to variables. Begins steganography.

            Parameters:
                argDict: dictionary of arguments provided
                mode: boolean to decide encoding or decoding. True to encode, False to decode

            Returns:
                String path of output file
                or (based on mode)
                String message and boolean message type. True for message, False for file
    '''
    # Get values from argDict
    startImage = argDict['inputs']   # Image inputted
    message = argDict['message']    # Message to hide, either file or string
    outFile = argDict['out']        # Image file to output to

    # Check data to determine what to do
    if mode:
        # Hide message in image
        logging.debug("Mode: Encoding text into image")
        # Check file: or str:
        if message[:4] == "str:":
            mType = True
            message = message[4:]
        elif message[:5] == "file:":
            mType = False
            message = message[5:]
        else:
            logging.error("Bad message provided")
            sys.exit(1)
        encodedImage = encode_text(startImage, message, mType)
        cv2.imwrite(outFile, encodedImage)
        return outFile

    elif not mode:
        # Unhide message from image
        logging.debug("Mode: Decoding message/file from image")
        decodedText, mType = decode_text(startImage)
        return decodedText, mType
