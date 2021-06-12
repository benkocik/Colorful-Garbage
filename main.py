'''
Programmers: Kyle Heestand and Ben Kocik
Description: 
'''
import argparse
import logging
import os
import sys
from datetime import datetime

def validateArguments(argDict: dict) -> None:
    '''
    Validates the current argument dictionary. If an argument is not valid, an exception should be raised.

            Parameters:
                argDict: dictionary of arguments to validate

            Returns:
                None
    '''
    
    if argDict['inputs'] == None:
        raise ValueError("Inputs can not be none! Please input at least 2 items", 'inputs')
    else:
        pass

    if len(argDict['inputs']) != 2:
        raise ValueError("Number of inputs must be 2, not " + len(argDict), 'inputs')
    else:
        pass
    # Restrict the inputs array to having the URIs str: and file:
    result = sum(map(lambda x: True if "str:" in x[:4] or "file:" in x[:5] else False, argDict['inputs']))
    if result == 2:
        pass
    else:
        raise ValueError("Invalid URI detected. Valid URIs are \'str:\' and \'file:\'", 'inputs')
    # Restrict the inputs from having 2 str: URIs
    result = sum(map(lambda x: True if "str:" in x[:4] else False, argDict['inputs']))
    if result == 2:
        raise ValueError("Can not have 2 \'str:\' URIs", 'inputs')
    else:
        pass
    # Must have an out file specified
    if argDict['out'] == None:
        raise ValueError("No output file specified. Please specify and output file", 'out')
    else:
        pass
    # Number of process can not be None
    if argDict['process'] == None:
        raise ValueError("Number of processes should be a number 1 - 4", 'process')
    # Number of processes must be less than 4
    if int(argDict['process']) > 4:
        raise ValueError("Number of processes should be a number 1 - 4", 'process')
    else:
        pass
    # Logging level must be between 10 and 50
    if not argDict['verbose'] in list(range(10,60,10)):
        raise ValueError("Verbose value must be DEBUG, INFO,  WARN, ERROR or CRITICAL", 'verbose')
    else:
        pass
    
    return True
    

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
            validateArguments(argDict)
            quitLoop = True
        except ValueError as e:
            print(e.args[0])
            doKeyPrompt(e.args[1], argDict)

def getInput(prompt: str, defaultValue) -> any:
    '''
    Gets input from the user. If enter is pressed, defaultValue is returned, if default value is none, program will keep prompting user for input

            Parameters:
                prompt: Prompt to ask user
                defaultValue: Default value to be returned if no input is given

            Returns:
                None
    '''
    print(prompt)
    try:
        userInput = input(" > ")
    except KeyboardInterrupt:
        print("User initiated a program exit")
        sys.exit(1)
    # Keep prompting user for input if there is no default value
    # If there is a keyboard interrupt, program will exit with non 0 status code 
    if defaultValue == None:
        while userInput == "":
            try:
                print("This can not be skipped. Please enter a value or press Control + C to quit")
                userInput = input(" > ")
            except KeyboardInterrupt:
                print("User initiated a program exit")
                sys.exit(1)
    
    if userInput == "":
        return defaultValue
    else:
        return userInput

def doKeyPrompt(argKey : str, argDict : dict):
    '''
    Allows user to type manually type in values based on key

            Parameters:
                argKey: key to prompt input for
                argDict: dictionary of arguments from argparse

            Returns:
                None
    '''
    if argKey == 'inputs':
        inputs = []
        userInput = getInput("Enter first URI path to a file or string\nEX: file:/path/to/file or str:someString",  None)
        inputs.append(userInput)
        userInput = getInput("Enter first URI path to a file or string\nEX: file:/path/to/file or str:someString",  None)
        inputs.append(userInput)
        argDict[argKey] = inputs
    elif argKey == 'process':
        userInput = getInput("Enter number of processes for threading\nDefault is 1, max is 4",  1)
        argDict[argKey] = int(userInput)
    elif argKey == 'out':
        userInput = getInput("Enter path to output picture\nEX: /path/to/picture.bmp",  None)
        argDict[argKey] = userInput
    elif argKey == 'verbose':
        userInput = getInput("Enter logging verbosity level\nValid values are: DEBUG, INFO,  WARN, ERROR or CRITICAL",  logging.ERROR)
        # Parse input into logging terms
        value = logging.CRITICAL
        if userInput == "DEBUG":
            value = logging.DEBUG
        elif userInput == "INFO":
            value = logging.INFO
        elif userInput == "WARN":
            value = logging.WARN
        elif userInput == "CRITICAL":
            value = logging.CRITICAL
        else:
            value = logging.ERROR
        argDict[argKey] = value
    elif argKey == 'log':
        tmpLogPath = os.getcwd() + "\\" + datetime.now().strftime("%Y%m%d_%H:%M:%S_log.log")
        userInput = getInput("Enter path to log file\nEX: /path/to/logfile.log",  tmpLogPath)
        argDict[argKey] = userInput
    else:
        # TODO: Implement something. I think an exit would go good here
        print("Unknown key \'" + argKey + "\' was entered. Something is very wrong")
        sys.exit(2)
    print()

if __name__ == "__main__" :
    '''
    Main method for program. This will setup the arguments and environment for the program to run

            Parameters:
                None

            Returns:
                None
    '''
    # Set the logfile path to the current directory
    tmpLogPath = os.getcwd() + "\\" + datetime.now().strftime("%Y%m%d_%H:%M:%S_log.log")
    # Parse arguments with argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputs', nargs=2, help="Inputs for program")
    parser.add_argument('-n', '--process', type=int, help="Number of processes for the program to use.", )
    parser.add_argument('-o', '--out', type=str, help="File to write to")
    parser.add_argument('-v', '--verbose', type=str, help="Change output verbosity")
    parser.add_argument('-l', '--log', type=str, help="File to log to. You can also put STDOUT to log to STDOUT.")
    args = parser.parse_args()
    # Get arguments as a dictionary so it is easier to work with
    argsDict = args.__dict__
    runSetup(argsDict)


