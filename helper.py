from Crypto.Util import number
import random

def mod_inverse(a, m) : 
    a, m = int(a), int(m)
    a = a % m
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def get_key(bitlength):
    p = number.getPrime(bitlength)
    q = number.getPrime(bitlength)
    n = p*q
    phi = (p-1)*(q-1)
    
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)

    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    key, n = public_key
    ciphertext = [ord(c) ** key % n for c in plaintext]
    return ciphertext

def decrypt(public_key, ciphertext):
    key, n = public_key
    plaintext = [chr((c ** key) % n) for c in ciphertext]
    return ''.join(plaintext)

public_key = get_key(8)
text = 'helloworld'
ciphertext = encrypt(public_key, text)
print(ciphertext)
plaintext = decrypt(public_key, text)
print(plaintext)