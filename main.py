'''
Programmers: Kyle Heestand and Ben Kocik
Description: 
'''
import argparse
import os
from PIL.Image import merge
import hashlib
import sys
from datetime import datetime
from validation import validate
from cryptoUtils import writeKey
import utils
from steganography import steganography

def doUnhide(argDict : dict):
    dateFromImage = steganography(argDict, False)
    #if argDict.__contains__

def doHide(argDict : dict):
    pass

def runSetup(argDict: dict):
    '''
    Runs a setup for any of the missing arguments. User will be able to manually type in missing values

            Parameters:
                argDict: dictionary of arguments from argparse

            Returns:
                None
    '''
    quitLoop = False
    while not quitLoop:
        try:
            validate(argDict)
            quitLoop = True
        except ValueError as e:
            doKeyPrompt(e.args, argDict)

def doKeyPrompt(exceptionArgs : tuple, argDict : dict):
    '''
    Allows user to type manually type in values based on key

            Parameters:
                exceptionArgs: arguments from thrown valueException
                argDict: dictionary of arguments from argparse

            Returns:
                None
    '''
    print("Exception thrown from key " + exceptionArgs[1])
    print(exceptionArgs[0])
    argDict[exceptionArgs[1]] = exceptionArgs[2](*exceptionArgs[3])

if __name__ == "__main__" :
    '''
    Main method for program. This will setup the arguments and environment for the program to run

            Parameters:
                None

            Returns:
                None
    '''
    # Set the logfile path to the current directory
    tmpLogPath = os.path.join(os.getcwd(), datetime.now().strftime("%Y%m%d_%H:%M:%S_log.log"))
    # Parse arguments with argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputs', help="Inputs for program")
    parser.add_argument('-n', '--process', type=int, help="Number of processes for the program to use.")
    parser.add_argument('-m', '--message', type=str, help="Message or file to hide. Messages must begin with str:/ files must begin with file:/")
    parser.add_argument('-o', '--out', type=str, help="File to write output image to")
    parser.add_argument('-v', '--verbose', type=int, help="Change output verbosity. Valid arguments are 10, 20, 30, 40 and 50")
    parser.add_argument('-l', '--log', type=str, help="File to log to. You can also put STDOUT to log to STDOUT.")
    parser.add_argument('-e', '--encrypt', type=str, help="Encrypt the data before hiding. A path to a key file is required here. Keys can be generate using the --gen-key flag")
    parser.add_argument('-d', '--decrypt', type=str, help="Decrypt the data after revealing. A path to a key file is required for this")
    parser.add_argument('--gen-key', type=bool, help="Generates a key to a specific file path for encryption")
    args = parser.parse_args()
    # Get arguments as a dictionary so it is easier to work with
    argsDict = args.__dict__
    print(argsDict.__contains__("decrypt"))
    print(argsDict)
