def encrypt(text_to_encrypt, key):
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
    for char in intermediate:
        # Check if the character is an alphabet letter.
        if char.isalpha():
            # Determine the shift amount based. i.e the amount of times to be shifted e.g 2,3,4....
            shift = key
            # Check if the character is a lowercase letter.
            if char.islower():
                # Apply Caesar cipher transformation for lowercase letters.
                result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                # Apply Caesar cipher transformation for uppercase letters.
                result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            # Preserve non-alphabet characters as they are.
            result += char
    # Return the encrypted or decrypted result.
    return result

def decrypt(text_to_decrypt, key):
    result = ""
    intermediate = ""
    # Encrypt the user's input using the specified key.
    for char in text_to_decrypt:
        # Check if the character is an alphabet letter.
        if char.isalpha():
            # Determine the shift amount based. i.e the amount of times to be shifted e.g 2,3,4....
            shift = -key
            # Check if the character is a lowercase letter.
            if char.islower():
                # Apply Caesar cipher transformation for lowercase letters.
                intermediate += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                # Apply Caesar cipher transformation for uppercase letters.
                intermediate += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            # Preserve non-alphabet characters as they are.
            intermediate += char
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
    return result