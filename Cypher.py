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
        temp_key = input("Please specify the shift length: ")
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
        temp_key = input("Please specify the shift length: ")
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
            print("Understood")
            a = True
            b = False
        elif loop == "N":
            print("Understood\nGoodbye")
            a = False
            b = False
        else:
            print(f"{Fore.RED}[!] Invalid input, please try again")
    return a

print(f"{Fore.WHITE}Welcome to Caesar Cypher Encryption/Decryption")
while a == True:
    cryption = input("Would you Encrypt or Decrypt\nType 'E' or 'D' ")
    if cryption == "E":
        encrypt()
        a = loop() 
    elif cryption == "D":
        decrypt()
        a = loop() 
    else:
        print(f"{Fore.RED}[!] Invalid input, please try again")