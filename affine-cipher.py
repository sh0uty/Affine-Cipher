def main():
    """
    Plain/Ciphertext in lowercase [a-z]
    
    """
    #print(Encrypt(Encrypt('k', 3, 5), 11, 7))
    #print(Decrypt('k', 0, 10))

def Encrypt(plain : str, a : int, b : int) -> str:
    ciphertext = ''
    for char in plain:
        ciphertext += chr( ( ( a * ( ord( char ) - 97 ) + b ) % 26 ) + 97 )
    return ciphertext

def Decrypt(cipher : str, a : int, b : int) -> str:
    inverse = Inverse(a)
    print(inverse)
    plaintext = ''

    for char in cipher:
        plaintext += chr(((((ord(char) - 97) - b) * inverse) % 26) + 97 )
    
    return plaintext

def Inverse(a : int) -> int:
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            return i
    raise Exception(f"No inverse of {a} found.")

if __name__ == '__main__':
    main()