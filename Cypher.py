"""
Cypher.py.

This is a program designed to perform Caesar Cypher operations.
"""

import cypher_helper
from colorama import Fore, init  # Import the colorama for colored text
init()  # Initialize the colorama library for colored text.

a = True  # This is for looping things


def encrypt(file_read):
    """
    Encrypt.

    This is the interface for encryption.
    """
    a = True
    if file_read is True:
        with open('Text_Insert.txt', 'r') as r:
            text_to_encrypt = r.readline()
    else:
        text_to_encrypt = input(f"{Fore.WHITE}Please Enter your text/message: ")
    while a is True:
        temp_key = input(f"{Fore.WHITE}Please specify the shift length: ")
        if temp_key.isdigit():
            key = int(temp_key)
            if key > 25 or key < 0:
                print(f"{Fore.RED}[!] Your shift length should be an integer number between 0 and 25 ")
            else:
                a = False
        else:
            print(f"{Fore.RED}[!] Your shift length should be an integer number between 0 and 25 ")
    encrypted_text = cypher_helper.encrypt(text_to_encrypt, key)
    print(f"{Fore.YELLOW}{text_to_encrypt} {Fore.WHITE}has been encrypted as {Fore.YELLOW}{encrypted_text}")
    with open('Cypher_Log.txt', 'a') as w:
        w.write(encrypted_text)
        w.write("\n")


def decrypt(file_read):
    """
    Decrypt.

    This is the interface for decryption.
    """
    a = True
    if file_read is True:
        with open('Text_Insert.txt', 'r') as r:
            text_to_decrypt = r.readline()
    else:
        text_to_decrypt = input(f"{Fore.WHITE}Please Enter your text/message: ")
    while a is True:
        temp_key = input(f"{Fore.WHITE}Please specify the shift length: ")
        if temp_key.isdigit():
            key = int(temp_key)
            if key > 25 or key < 0:
                print(f"{Fore.RED}[!] Your shift length should be an integer number between 0 and 25 ")
            else:
                a = False
        else:
            print(f"{Fore.RED}[!] Your shift length should be an integer number between 0 and 25 ")
    decrypted_text = cypher_helper.decrypt(text_to_decrypt, key)
    print(f"{Fore.YELLOW}{text_to_decrypt} {Fore.WHITE}has been decrypted as {Fore.YELLOW}{decrypted_text}")
    with open('Cypher_Log.txt', 'a') as w:
        w.write(decrypted_text)
        w.write("\n")


def loop():
    """
    Loop.

    This is to perform repeat operations.
    """
    b = True
    while b is True:
        loop = input(f"{Fore.WHITE}Would you like to perform another Encryption or Decryption\nType 'Y' or 'N' ")
        loop = loop.upper()
        if loop == "Y":
            print(f"{Fore.WHITE}Understood")
            a = True
            b = False
        elif loop == "N":
            print(f"{Fore.WHITE}Understood\nGoodbye")
            with open('Cypher_Log.txt', 'a') as w:
                w.write("----------------------------------")
                w.write("\n")
            a = False
            b = False
        else:
            print(f"{Fore.RED}[!] Invalid input, please try again")
    return a


print(f"{Fore.WHITE}Welcome to Caesar Cypher Encryption/Decryption")
print(f"{Fore.WHITE}Please note that non-english letters will not function properly")
# \/ If you would like to read from the file
while a is True:
    file_read = input(f"{Fore.WHITE}Would you like to use a file to Perform an Encryption/Decryption\nType 'Y' or 'N' ")
    file_read = file_read.upper()
    if file_read == "Y":
        print(f"{Fore.WHITE}Please confirm that the text has been written to {Fore.YELLOW}Text_Insert.txt")
        print(f"{Fore.WHITE}Make sure to save and also note that only the first line will be used")
        file_read = True
        a = False
    elif file_read == "N":
        print(f"{Fore.WHITE}Understood")
        file_read = False
        a = False
    else:
        print(f"{Fore.RED}[!] Invalid input, please try again")
a = True   # I need to reset it
# \/ The main interface
while a is True:
    cryption = input(f"{Fore.WHITE}Would you like to Encrypt or Decrypt\nType 'E' or 'D' ")
    cryption = cryption.upper()
    if cryption == "E":
        encrypt(file_read)
        a = loop()
    elif cryption == "D":
        decrypt(file_read)
        a = loop()
    else:
        print(f"{Fore.RED}[!] Invalid input, please try again")
