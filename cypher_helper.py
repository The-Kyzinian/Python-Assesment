"""
Cypher Helper.

This is where the actual encryption/decryption occurs.
"""


def encrypt(text_to_encrypt, key):
    """
    Encrypt.

    This is the encryption code, with Therinas.
    """
    result = ""
    intermediate = ""
    # \/ This is Therinas, it is for basic frecuency analysis prevention
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
        elif char == "A":
            intermediate += "S"
        elif char == "a":
            intermediate += "s"
        elif char == "S":
            intermediate += "A"
        elif char == "s":
            intermediate += "a"
        else:
            intermediate += char
    for char in intermediate:
        if char.isalpha():
            shift = key
            if char.islower():
                result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            result += char
    return result


def decrypt(text_to_decrypt, key):
    """
    Decrypt.

    This is the decryption code, with Therinas.
    """
    result = ""
    intermediate = ""
    for char in text_to_decrypt:
        if char.isalpha():
            shift = -key
            if char.islower():
                intermediate += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                intermediate += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            intermediate += char
    # \/ Therinas again
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
        elif char == "A":
            result += "S"
        elif char == "a":
            result += "s"
        elif char == "S":
            result += "A"
        elif char == "s":
            result += "a"
        else:
            result += char
    return result
