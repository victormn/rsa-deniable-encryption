"""
Development file to implement a deniable encryption cryptosystem
"""

import math
import random
from decimal import Decimal, getcontext
from functools import reduce

getcontext().prec = 20

def get_gcd(*numbers):
    """Return the greatest common divisor from numbers."""
    from fractions import gcd
    return reduce(gcd, numbers)

def get_lcm(*numbers):
    """Return the least common multiple from numbers."""
    def lcm(a, b):
        return (a * b) // get_gcd(a, b)
    return reduce(lcm, numbers, 1)

def multiplicative_inverse(e, phi):
    """Return a multiplicative inverse of e mod phi."""
    x = 0
    y = 1
    old = phi
    while phi != 0:
        q = e // phi
        (e, phi) = (phi, e % phi)
        (x, y) = ((y - (q * x)), x)

    if y < 0:
        y = y + old

    return y

def create_sieve(n):
    """Return all primes <= n."""
    np1 = n + 1
    s = list(range(np1)) 
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)

def rand_prime(size, sieve):
    """Return a random prime >= size using a sieve set."""
    rand = random.randrange(2**(size-2), 2**size)
    while not rand in sieve:
        rand += 1
    return rand

def generate_keypair(size):
    """Generates RSA public and private key."""
    sieve = set(create_sieve(2**size))
    p = rand_prime(size, sieve)
    q = rand_prime(size, sieve)

    if p > q:
        (p, q) = (q, p)

    n = p * q
    phi = get_lcm((p-1), (q-1))
    e = 65537
    g = get_gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = get_gcd(e, phi)

    d = multiplicative_inverse(e, phi)
    return ({'e': e, 'N': n}, {'d': d, 'N': n})

def encryption(m, e, N):
    """Encrypt message m as follow:
    C = (m ** e) mod N."""
    return pow(m, e, N)

def decryption(c, d, N):
    """Decrypt cipher c as follow:
    M = (c ** d) % N."""
    if d == (d//1):
        return pow(c, d, N)

    return round((c**d) % N)

def collision_finder(m2, c, N):
    """Find a RSA key parameter D such that the message m2 can be decrypted from cipher c
    D2 = log(m2 + N) / log(C)."""
    return Decimal(Decimal(math.log(m2 + N))/Decimal(math.log(c)))

def main():
    """Do main stuffs (just for development)."""
    pk, sk = generate_keypair(22)

    print("e:   ", pk['e'])
    print("N:   ", pk['N'])
    print("d:   ", sk['d'])

    print()

    m1 = 1234567890
    print("m:   ", m1)
    c = encryption(m1, pk['e'], pk['N'])
    print("c:   ", c)
    mf = decryption(c, sk['d'], pk['N'])
    print("m:   ", mf)

    print()

    m2 = 9876543210
    print("m2:  ", m2)
    sk_d2 = collision_finder(m2, c, pk['N'])
    print("d2:  ", sk_d2)
    mf2 = decryption(c, sk_d2, pk['N'])
    print("m2:  ", mf2)

if __name__ == '__main__':
    main()
