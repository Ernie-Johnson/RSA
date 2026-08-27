from modexp import mod_pow

def encrypt(message, public_key):
    n, e = public_key
    return(mod_pow(message, e, n))

def decrypt(ciphertext, private_key):
    n, d = private_key
    return(mod_pow(ciphertext, d, n))