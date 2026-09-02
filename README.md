# RSA
Building the RSA encryption algorithm from scratch

[Research was done from this paper](https://www.math.uchicago.edu/~may/VIGRE/VIGRE2007/REUPapers/FINALAPP/Calderbank.pdf)

## What I accomplished in this project
- Can generate RSA public/private keypairs at any key size
- Used chunking to enable myself to encrypt and decrypt messages of arbitrary length
- Implemented Miller-Rabin primality testing from scratch

## Design decisions
I used 65537 as the exponent for the public key since it is prime so checking it is coprime with φ(n) is almost certain. The fact it is fixed also doesn't weaken the encryption since we are relying on the fact n is difficult to factor causing it to be difficult to find the multiplicative inverse of the exponent under mod φ(n)

I used the Miller-Rabin primality test because it helps to prevent from Carmichael numbers falsely registering as prime

I used PKCS#7-style padding because the messages sent need to be split into fixed-sized chunks before they are encrypted and the final chunk usually isn't a multiple of the chunk size. Therefore I can avoid having to transmit the original message length I set each padding byte to the value of the padding length therefore when receiving the message the last byte just needs to be checked to know how much to strip from the message. In the case the message divides evenly a whole extra chunk of padding is added.

