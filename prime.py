from modexp import mod_pow
import random

def is_prime(n, rounds):
    if n < 4:
            return n in (2, 3)
    if (n % 2 == 0):
        return False
    
    n_temp = n - 1
    s = 0
    d = 0
    
    while True:
        if(n_temp % 2 == 0):
            s += 1
            n_temp //= 2
        else:
            d = n_temp
            break

    for i in range(rounds):
        a = random.randint(2, n-2)
        a_result = is_composite_witness(a, d, s, n)
        if(a_result):
            return False
    return True


def is_composite_witness(a, d, s, n):
    x = mod_pow(a, d, n)
    if(x == 1 or x == n-1):
        return False
    for i in range(s-1):
        x = mod_pow(x, 2, n)
        if(x == n-1):
            return False
    return True
    
    