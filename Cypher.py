import cypher_helper
from colorama import Fore, init  # Import the colorama for colored text
init()  # Initialize the colorama library for colored text.

a = True

def encrypt():
    a = True
    # Prompt the user to enter the text to be encrypted        
    text_to_encrypt = input(f"{Fore.WHITE}Please Enter your text/message: ")
    # Prompt the user to specify the shift length (the key).
    while a == True:
        temp_key = input(f"{Fore.WHITE}Please specify the shift length: ")
        if temp_key.isdigit():
            key = int(temp_key)
            # Check if the specified key is within a valid range (0 to 25).
            if key > 25 or key < 0:
                # Display an error message if the key is out of range.
                print(f"{Fore.RED}[!] Your shift length should be a number between 0 and 25 ")
            else:
                a = False
        else:
            print(f"{Fore.RED}[!] Your shift length should be a number between 0 and 25 ")
        # Encrypt the user's input using the specified key.
    encrypted_text = cypher_helper.encrypt(text_to_encrypt,key)
    print(f"{Fore.YELLOW} {text_to_encrypt} {Fore.WHITE}has been encrypted as {Fore.YELLOW}{encrypted_text}")

def decrypt():
    a = True
    # Prompt the user to enter the text to be encrypted        
    text_to_decrypt = input(f"{Fore.WHITE}Please Enter your text/message: ")
    # Prompt the user to specify the shift length (the key).
    while a == True:
        temp_key = input(f"{Fore.WHITE}Please specify the shift length: ")
        if temp_key.isdigit():
            key = int(temp_key)
            # Check if the specified key is within a valid range (0 to 25).
            if key > 25 or key < 0:
                # Display an error message if the key is out of range.
                print(f"{Fore.RED}[!] Your shift length should be a number between 0 and 25 ")
            else:
                a = False
        else:
            print(f"{Fore.RED}[!] Your shift length should be a number between 0 and 25 ")
    decrypted_text = cypher_helper.decrypt(text_to_decrypt, key)
    # Display the encrypted text.
    print(f"{Fore.YELLOW} {text_to_decrypt} {Fore.WHITE}has been decrypted as {Fore.YELLOW}{decrypted_text}")

def loop():
    b = True
    while b == True:
        loop = input(f"{Fore.WHITE}Would you like to preform another Encryption or Decryption\nType 'Y' or 'N' ")
        if loop == "Y":
            print(f"{Fore.WHITE}Understood")
            a = True
            b = False
        elif loop == "N":
            print(f"{Fore.WHITE}Understood\nGoodbye")
            a = False
            b = False
        else:
            print(f"{Fore.RED}[!] Invalid input, please try again")
    return a

print(f"{Fore.WHITE}Welcome to Caesar Cypher Encryption/Decryption")
while a == True:
    file_read = input(f"{Fore.WHITE}Would you like to use a file to Perform an Encryption/Decryption\nType 'Y' or 'N' ")
    if file_read == "Y":
        print(f"{Fore.WHITE}Please confirm that the text has been written to {Fore.YELLOW}Text_Insert.txt")
        print(f"{Fore.WHITE}Also note that only the first line will be used")
        file_read =True
        a = False
    elif file_read == "N":
        print(f"{Fore.WHITE}Understood")
        file_read = False
        a = False
    else:
        print(f"{Fore.RED}[!] Invalid input, please try again")
a = True
while a == True:
    cryption = input(f"{Fore.WHITE}Would you like to Encrypt or Decrypt\nType 'E' or 'D' ")
    if cryption == "E":
        encrypt()
        a = loop() 
    elif cryption == "D":
        decrypt()
        a = loop() 
    else:
        print(f"{Fore.RED}[!] Invalid input, please try again")