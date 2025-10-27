def encrypt_caesar(plaintext: str, shift = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    if (plaintext == ""):
        ciphertext = ""
    else:
        for  i in range(len(plaintext)):
                f = False
                sym = ord(plaintext[i])
                n_sym = 0
            
                
                if 65 <= sym <= (90 - shift): 
                    n_sym = sym + shift
                    f = True
                elif ((90 - shift) <= sym <= (90 + shift)):
                    n_sym = (65 + sym - 88)
                    f = True
                if ( (f == False) and (97 <= sym <= (122 - shift)) ):
                    n_sym = sym + shift
                    f = True
                elif ( (f == False) and ((122 - shift) <= sym <= (122 + shift)) ):
                    n_sym = 97 + (sym - 119) - 1
                    f = True
                    
                if (f == False):
                    n_sym = sym

                ciphertext += chr(n_sym)
    return ciphertext
        



def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    if (ciphertext == ""):
        plaintext = ""
    else:
        for  i in range(len(ciphertext)):
                f = False
                sym = ord(ciphertext[i])
                n_sym = 0
            
                
                if ((65 + shift) <= sym <= 90): 
                    n_sym = sym - shift
                    f = True
                elif ((65 - shift) <= sym <= (65 + shift - 1)):
                    n_sym = (65 + (90 - sym))
                    f = True
                if ( (f == False) and ((97 + shift) <= sym <= 122) ):
                    n_sym = sym - shift
                    
                    f = True
                elif ( (f == False) and (97 - shift) <= sym <= (97 + shift - 1) ):
                    n_sym = (97 + (122 - sym))
                    f = True
                    
                if (f == False):
                    n_sym = sym

                plaintext += chr(n_sym)
    
    return plaintext




