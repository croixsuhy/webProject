from cryptography.fernet import Fernet as Fer
from datetime import datetime
import pickle
import os

"""------------------------------------------------------"""
# Time to make key expire, change to whatever you want here
# If you set it to None it will never expire
# Time is in minutes
EXPIRATION_TIME = 1
"""------------------------------------------------------"""


def expirationTime():
    global listTime  # Globalize expiration time

    try:
        with open("time.txt", "w") as timeFile:
            # Get current time in hours and minutes
            time = datetime.now()
            timeFile.write(time.strftime("%H:%M"))  # Hours : Minutes

            # Split into a list, create time to expire
            listTime = time.strftime("%H:%M").split(":")

            # If there is a leading zero in the minutes, only use the first number (leading zeros illegal in python)
            listTime[1] = str(eval(f"{listTime[1][1] if listTime[1][0] == '0' else listTime[1]} + {EXPIRATION_TIME}"))

    except OSError:
        print("Can't write to \"time.txt\"")


def existingTime():
    global listTime  # Globalize expiration time

    with open("time.txt", "r") as timeFile:
        # Create time to expire
        listTime = timeFile.read().split(":")

        # If there is a leading zero in the minutes, only use the first number (leading zeros illegal in python)
        listTime[1] = str(eval(f"{listTime[1][1] if listTime[1][0] == '0' else listTime[1]} + {EXPIRATION_TIME}"))


def createKey():
    global f  # Globalize key

    try:
        # Open, generate key, and write to file
        with open("key.txt", "rb") as keyFile:
            key = Fer.generate_key()

            # Sometimes Fernet likes to generate the same key, so we keep generating until we get a different key
            while keyFile.read() == key:
                key = Fer.generate_key()

        with open("key.txt", "wb") as keyFile:
            f = Fer(key)
            keyFile.write(key)

    except OSError:
        print("Can't write to or create \"pickledData.txt\"")


def existingKey():
    global f  # Globalize key
    # Make existing key in text file the actual key

    with open("key.txt", "rb") as keyFile:
        key = keyFile.read()
        f = Fer(key)


def encrypt():
    data = input("Enter what you want encrypted and serialized: ").encode()  # Encoding turns string into bytes

    # Encrypt the data
    encryptedData = f.encrypt(data)

    if os.path.getsize("pickledData.txt") == 0:
        # Create list if text file is empty
        dataList = []

    else:
        with open("pickledData.txt", "rb") as dataFile:
            dataList = list(pickle.load(dataFile))  # Load existing data

    # Pickle the encrypted data
    with open("pickledData.txt", "wb") as dataFile:
        try:
            dataList.append(encryptedData)  # Add data to list
            pickle.dump(dataList, dataFile)  # Dump data

        except RuntimeError:
            print("Can't dump data to \"pickledData.txt\"")

    decrypt = input("Decrypt data? (Y/N/clear): ")

    if decrypt.lower() == "y":
        try:
            with open("pickledData.txt", "rb") as dataFile:
                # Unpickle and print decrypted data in list
                for data in pickle.load(dataFile):
                    try:
                        print(f.decrypt(data))
                    except:
                        print("Can't decrypt")

        except RuntimeError:
            print("\"pickledData.txt\" is empty")

    elif decrypt.lower() == "n":
        try:
            with open("pickledData.txt", "rb") as dataFile:
                # Unpickle and print encrypted data in list
                for data in pickle.load(dataFile):
                    print(data)

        except RuntimeError:
            print("\"pickledData.txt\" is empty")

    elif decrypt.lower() == "clear":
        try:
            # Clear data in the text file
            with open("pickledData.txt", "wb") as dataFile:
                dataFile.write(b"")

        except RuntimeError:
            print("\"pickledData.txt\" can't be cleared")


def again():
    # Asks user if they want to do it again
    encryptMore = input("\nWould you like to encrypt more? (Y/N)\n")

    if encryptMore.lower() == "y":
        main()  # If so, run main


def main():
    try:
        # Check and see if both are empty, if so create a new key/expiration time, else, use the one made before
        if os.path.getsize("time.txt") == 0:
            expirationTime()
        else:
            existingTime()

        if os.path.getsize("key.txt") == 0:
            createKey()
        else:
            existingKey()

    except RuntimeError:
        print("Can not open \"time.txt\" or \"key.txt\"")

    # Check to see if the time is before the expiration time, if not, generate new key and expiration time
    if EXPIRATION_TIME == None:
        pass

    else:
        if listTime <= datetime.now().strftime("%H:%M").split(":"):
            # Create new key and expiration time for key
            print("WARNING: Key expired")
            print("Generating new key...")

            expirationTime()
            createKey()

            print("Done! If you try to decrypt past data, it won't work.\n")

            encrypt()
            again()

        else:
            encrypt()
            again()


main()
