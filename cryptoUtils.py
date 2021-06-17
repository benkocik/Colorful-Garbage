from cryptography.fernet import Fernet

def writeKey(keyFilePath : str):
    """
    Generates an AES farnet key and save it into a file

            Parameters:
                keyFilePath: path to key file to write to

            Returns:
                None
    """
    key = Fernet.generate_key()
    with open(keyFilePath, "w") as key_file:
        key_file.write(key.decode())

def loadKey(keyFilePath : str) -> bytes:
    """
    loads an AES farnet key and from a file

            Parameters:
                keyFilePath: path to key file to write to

            Returns:
                Key from file as bytes
    """
    return open(keyFilePath, "rb").read()

def encrypt(message : bytes, key : bytes):
    """
    Encrypts a message

            Parameters:
                message: the message to encrypt in bytes
                key: key to use
    """
    fernetKey = Fernet(key)
    return fernetKey.encrypt(message)

def decrypt(encryptedMessage : bytes, key : bytes):
    """
    Encrypts a message

            Parameters:
                message: the message to encrypt in bytes
                key: key to use
    """
    fernetKey = Fernet(key)
    return fernetKey.decrypt(encryptedMessage)