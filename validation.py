from os import path
import sys

def validate(dictionary : dict):
    '''
    Validates the current argument dictionary. If an argument is not valid, an exception will be raised.

            Parameters:
                argDict: dictionary of arguments to validate

            Returns:
                None
    '''
    
    if dictionary['inputs'] == None:
        raise ValueError("No input specified. Please specify an input file Ex \'/path/to/file.png\'", "inputs", getFilePath, ["file:"])

    if not "file:" in dictionary['inputs']:
        raise ValueError("Input must have \'file:/\' before the path. Ex \'/path/to/file.png\'", "inputs", getFilePath, ["file:"])

    if not path.exists(dictionary['inputs'].replace("file:","")):
        raise ValueError("Path to file does not exist. Please select a existing file.", "inputs", getFilePath, ["file:"])

    if dictionary['mode']:
        if "file:" in dictionary['message']:
            if not path.exists(dictionary['message'].replace("file:","")):
                raise ValueError("Path to file does not exist. Please enter a existing file.", "message", getFilePath, ["file:"])

        if (not "file:" in dictionary['message']) and (not "str:" in dictionary['message']):
            raise ValueError("Message must have a str: or file:", "message", getString, [""])

    if dictionary['process'] < 0 or dictionary['process'] > 4:
        raise ValueError("Number of processes must be a valid number between 1 and 4", "process", getInteger, [(1, 4), 1])

    if not dictionary['verbose'] in list(range(10,60,10)):
        raise ValueError("Invalid number for verbose level. Valid levels are 10,20,30,40 and 50", "verbose", getIntegerInRange, [(10, 50, 10), 50])

    if dictionary.__contains__("decrypt"):
        if not path.exists(dictionary['decrypt']):
            raise ValueError(dictionary['decrypt'] + " does not exist.", "decrypt", getFilePath, [""])
        if dictionary['decrypt'] == None:
            raise ValueError("Decrypt keyfile was not entered.", "decrypt", getFilePath, [""])

def getInteger(*args) -> int:
    '''
    Gets an integer from the user while checking if the entered information is valid. 
    If the user cancels this operation, program will close with exit status of 2. 
    An integer is valid if it is greater than or equal to the smallest value and less 
    than and equal to the largest value

            Parameters:
                boundTuple: Tuple with bounds ie (lowest value, highest value)
                defaultValue: default value to use if nothing is entered

            Returns:
                Entered integer
    '''
    print("Enter a integer below or press Control + C to quit")
    if(args[1] != None):
        print("You can also press Enter to use the default value of " + str(args[1]))
    integerInput = args[0][0]
    endLoop = False
    while not endLoop:
        try:
            userInput = input(" > ")
            if userInput == "":
                if args[1] != None:
                    integerInput = args[1]
                    endLoop = True
                else:
                    print("Enter a valid integer")
            else: 
                integerInput = int(userInput)
                if integerInput >= args[0][0] and integerInput <=args[0][1]:
                    endLoop = True
                else:
                    if(args[1] != None):
                        print("Enter a valid integer between " + str(args[0][0]) + " and " + str(args[0][1]))
                    else:
                        print("Enter a valid integer")

        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Exiting program")
            sys.exit(2)
        except ValueError:
            if(args[1] != None):
                print("Enter a valid integer between " + str(args[0][0]) + " and " + str(args[0][1]))
            else:
                print("Enter a valid integer")

    return integerInput

def getIntegerInRange(*args) -> int:
    '''
    Gets an integer from the user while checking if the entered information is valid. 
    If the user cancels this operation, program will close with exit status of 2. 
    An integer is valid if it is greater than or equal to the smallest value and less 
    than and equal to the largest value

            Parameters:
                boundTuple: Tuple with bounds ie (lowest value, highest value)
                defaultValue: default value to use if nothing is entered

            Returns:
                Entered integer
    '''
    generatedRange = list(range(args[0][0], args[0][1] + 1))
    if not args[0][2] is None:
        generatedRange = list(range(args[0][0], args[0][1] + 1, args[0][2]))
    print("Enter a integer below or press Control + C to quit")
    if(args[1] != None):
        print("You can also press Enter to use the default value of " + str(args[1]))
    integerInput = args[0][0]
    endLoop = False
    while not endLoop:
        try:
            userInput = input(" > ")
            if userInput == "":
                if args[1] != None:
                    integerInput = args[1]
                    endLoop = True
                else:
                    if(args[1] != None):
                        print("Enter a valid integer between " + str(args[0][0]) + " and " + str(args[0][1]))
                    else:
                        print("Enter a valid integer")
            else: 
                integerInput = int(userInput)
                if integerInput in generatedRange:
                    endLoop = True

        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Exiting program")
            sys.exit(2)
        except ValueError:
            if(args[1] != None):
                print("Enter a valid integer between " + str(args[0][0]) + " and " + str(args[0][1]))
            else:
                print("Enter a valid integer")

    return integerInput

def getFilePath(*args) -> str:
    '''
    Gets a file path from the user while checking if the file path is valid. If the user cancels this operation, program will close with exit status of 2

            Parameters:
                appendBefore: String to append before the returned path

            Returns:
                Entered file path as a string
    '''
    print("Enter a valid file path below or press Control + C to quit:")
    userInput = ""
    while not path.exists(userInput):
        try:
            userInput = input(" > ")
        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Exiting program")
            sys.exit(2)

    return args[0] + userInput

def getString(*args) -> str:
    '''
    Gets a string from the user

            Parameters:
                None

            Returns:
                Entered entered string
    '''
    print("Enter a valid input below or press Control + C to quit:")
    userInput = ""
    while userInput == "":
        try:
            userInput = input(" > ")
        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Exiting program")
            sys.exit(2)
    
    return userInput
