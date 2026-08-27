import sympy
import random
from modexp import mod_inverse

def generate_keypair(bit_length):
    e = 65537
    while True:
        p = random.getrandbits(bit_length) | 1 | (1 << (bit_length - 1))
        q = random.getrandbits(bit_length) | 1 | (1 << (bit_length - 1))
        while(not sympy.isprime(p) or not sympy.isprime(q)):
            p = random.getrandbits(bit_length) | 1 | (1 << (bit_length - 1))
            q = random.getrandbits(bit_length) | 1 | (1 << (bit_length - 1))
        n = p*q
        phi_n = (p-1)*(q-1)
        try:
            d = mod_inverse(e, phi_n)
            break
        except ValueError:
            continue
    return (n, e), (n, d) # public_key, private_key
