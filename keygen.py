import random
from modexp import mod_inverse
from prime import is_prime

def generate_keypair(bit_length, rounds=40):
    e = 65537
    while True:
        p = random.getrandbits(bit_length) | 1 | (1 << (bit_length - 1))
        q = random.getrandbits(bit_length) | 1 | (1 << (bit_length - 1))
        while(not is_prime(p, rounds) or not is_prime(q, rounds)):
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
