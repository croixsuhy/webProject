from cryptography.fernet import Fernet as Fer
# import os

text = []
encryptedText = []

# Define key out of loop
key = None

# Determines if we generate a random key or not
rKey = None

try:
    # Open file and examine the contents and add them to a list to be encrypted
    with open("test.txt", "rb") as decryptedFile:
        for line in decryptedFile:
            # Check for a key
            if line[:7] == b"key = \"":

                # Check to see if we have any tab or break spaces
                if line[-2:] == b"\r\n":
                    key = line[:-2]
                else:
                    key = line

                break  # Break so we don't go back and reverse the value back to None
            else:
                key = None

    with open("test.txt", "rb") as decryptedFile:
        for line in decryptedFile:
            if line[-2:] == b"\r\n":
                text.append(line[:-2])
            else:
                text.append(line)

            # If it doesn't have a key, then pass
            if key is None:
                pass
            elif key[:-2] == b"\r\n":
                key = key[:-2]

    if key is not None:
        key = key[7:-1]
        rKey = False
    else:
        print("WARNING! No key!!! Generating random key...")
        rKey = True

    if not text:
        print("Nothing to encrypt")

    else:

        """ ~~~~~~ Encryption ~~~~~~ """
        ################################

        for word in text:

            # Ignore encrypting the key
            if word[:7] == b"key = \"":
                pass
            else:
                if rKey:
                    # If we don't have a key, create a random key
                    key = Fer.generate_key()

                f = Fer(key)

                print(f.encrypt(word))



except RuntimeError:
    print("Can't do anything")  # Used as a safety net
