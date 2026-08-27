def mod_pow(base, exp, mod):
    result = 1
    currentPower = base
    while(exp > 0):
        if(exp % 2 == 1):
            result *= currentPower
            result = result % mod
        currentPower *= currentPower
        currentPower = currentPower % mod # mod stops value from blowing up
        exp = exp // 2 # gives the next bit of the exponent
    return result


def extended_gcd(a, b): # returns the bezout for a and b
    if(b == 0):
        return(a, 1, 0)
    gcd, x1, y1 = extended_gcd(b, a%b)
    x = y1
    y = x1 - (a//b)*y1
    return (gcd, x, y)
