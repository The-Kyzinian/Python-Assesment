from colorama import Fore, init  # Import the colorama for colored text
init()  # Initialize the colorama library for colored text.

a = True
def implement_caesar_cipher(message, key, decrypt=False):
   # Initialize an empty string to store the result.
   result = ""
   # Iterate through each character in the user's input message.
   for character in message:
       # Check if the character is an alphabet letter.
       if character.isalpha():
           # Determine the shift amount based. i.e the amount of times to be shifted e.g 2,3,4....
           shift = key if not decrypt else -key
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
   return result  # Return the encrypted or decrypted result.

def encrypt(text_to_encrypt):
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
    encrypted_text = implement_caesar_cipher(text_to_encrypt, key)
    # Display the encrypted text.
    print(f"{Fore.YELLOW} {text_to_encrypt} {Fore.WHITE}has been encrypted as {Fore.YELLOW}{encrypted_text}")

def decrypt(text_to_decrypt):
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
    # Encrypt the user's input using the specified key.
    decrypted_text = implement_caesar_cipher(text_to_decrypt, key, decrypt=True)
    # Display the encrypted text.
    print(f"{Fore.YELLOW} {text_to_decrypt} {Fore.WHITE}has been encrypted as {Fore.YELLOW}{decrypted_text}")

print(f"{Fore.WHITE}")
while a == True:
    cryption = ("Would you Encpypt or Decrypt\nType 'E' or 'D'")
    if cryption == "E":
        encrypt
    elif cryption == "D":
        decrypt
    else:
        print(f"{Fore.RED}[!] Invalid input, please try again")