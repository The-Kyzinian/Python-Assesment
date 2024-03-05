from colorama import Fore, init  # Import the colorama for colored text
init()  # Initialize the colorama library for colored text.

a = True

def encrypt():
    a = True
    # Prompt the user to enter the text to be encrypted        
    text_to_encrypt = input(f"{Fore.WHITE}Please Enter your text/message: ")
    # Prompt the user to specify the shift length (the key).
    while a == True:
        key = int(input("Please specify the shift length: "))
        # Check if the specified key is within a valid range (0 to 25).
        if key > 25 or key < 0:
            # Display an error message if the key is out of range.
           print(f"{Fore.RED}[!] Your shift length should be between 0 and 25 ")
        else:
            a = False
        # Encrypt the user's input using the specified key.
    result = ""
    intermediate = ""
    # Iterate through each character in the user's input message.
    for char in text_to_encrypt:
        if char == "E":
            intermediate += "R"
        elif char == "e":
            intermediate += "r"
        elif char == "R":
            intermediate += "E"
        elif char == "r":
            intermediate += "e"
        elif char == "T":
            intermediate += "H"
        elif char == "t":
            intermediate += "h"
        elif char == "H":
            intermediate += "T"
        elif char == "h":
            intermediate += "t"
        elif char == "I":
            intermediate += "N"
        elif char == "i":
            intermediate += "n"
        elif char == "N":
            intermediate += "I"
        elif char == "n":
            intermediate += "i"
        else:
            intermediate += char
    for character in intermediate:
        # Check if the character is an alphabet letter.
        if character.isalpha():
            # Determine the shift amount based. i.e the amount of times to be shifted e.g 2,3,4....
            shift = key
            # Check if the character is a lowercase letter.
            if character.islower():
                # Apply Caesar cipher transformation for lowercase letters.
                result += chr(((ord(character) - ord('a') + shift) % 26) + ord('a'))
            else:
                # Apply Caesar cipher transformation for uppercase letters.
                result += chr(((ord(character) - ord('A') + shift) % 26) + ord('A'))
        else:
            # Preserve non-alphabet characters as they are.
            result += character
    # Return the encrypted or decrypted result.
    encrypted_text = result
    print(f"{Fore.YELLOW} {text_to_encrypt} {Fore.WHITE}has been encrypted as {Fore.YELLOW}{encrypted_text}")

def decrypt():
    a = True
    # Prompt the user to enter the text to be encrypted        
    text_to_decrypt = input(f"{Fore.WHITE}Please Enter your text/message: ")
    # Prompt the user to specify the shift length (the key).
    while a == True:
        key = int(input("Please specify the shift length: "))
        # Check if the specified key is within a valid range (0 to 25).
        if key > 25 or key < 0:
            # Display an error message if the key is out of range.
           print(f"{Fore.RED}[!] Your shift length should be between 0 and 25 ")
        else:
            a = False
    result = ""
    intermediate = ""
    # Encrypt the user's input using the specified key.
    for character in text_to_decrypt:
        # Check if the character is an alphabet letter.
        if character.isalpha():
            # Determine the shift amount based. i.e the amount of times to be shifted e.g 2,3,4....
            shift = key
            # Check if the character is a lowercase letter.
            if character.islower():
                # Apply Caesar cipher transformation for lowercase letters.
                intermediate += chr(((ord(character) - ord('a') + shift) % 26) + ord('a'))
            else:
                # Apply Caesar cipher transformation for uppercase letters.
                intermediate += chr(((ord(character) - ord('A') + shift) % 26) + ord('A'))
        else:
            # Preserve non-alphabet characters as they are.
            intermediate += character
    for char in intermediate:
        if char == "E":
            result += "R"
        elif char == "e":
            result += "r"
        elif char == "R":
            result += "E"
        elif char == "r":
            result += "e"
        elif char == "T":
            result += "H"
        elif char == "t":
            result += "h"
        elif char == "H":
            result += "T"
        elif char == "h":
            result += "t"
        elif char == "I":
            result += "N"
        elif char == "i":
            result += "n"
        elif char == "N":
            result += "I"
        elif char == "n":
            result += "i"
        else:
            result += char
    decrypted_text = result
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