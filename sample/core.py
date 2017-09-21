"""
# TODO: Describe this project here
"""

import math
import random
from decimal import Decimal, getcontext
from functools import reduce
from Crypto.Util import number

getcontext().prec = 20

def gcd(*numbers):
    """# TODO: Describe this method here"""
    from fractions import gcd
    return reduce(gcd, numbers)

def lcm(*numbers):
    """# TODO: Describe this method here"""
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)

def multiplicative_inverse(exp, phi):
    """# TODO: Describe this method here"""
    aux1 = 0
    aux2 = 1
    old_phi = phi
    while phi != 0:
        aux3 = exp // phi
        (exp, phi) = (phi, exp % phi)
        (aux1, aux2) = ((aux2 - (aux3 * aux1)), aux1)

    if aux2 < 0:
        aux2 = aux2 + old_phi

    return aux2

def generate_keypair():
    """Generates RSA public and private key"""
    p = 33421979
    q = 58320289
    # p = q = 1
    # while number.size(p*q) < 52:
        # p = rand_prime(26)
        # q = rand_prime(26)

    if p > q:
        (p, q) = (q, p)

    n = p * q
    phi = lcm((p-1), (q-1))
    e = 65537
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)  
    return ({'e': e, 'N': n}, {'d': d, 'N': n})

def encryption(message, exp, modulus):
    """C = (message ** exp) mod modulus"""
    return pow(message, exp, modulus)

def decryption(cipher, exp, modulus):
    """M = (cipher ** exp) % modulus"""
    if exp == (exp//1):
        return pow(cipher, exp, modulus)

    return round((cipher**exp) % modulus)

def collision_finder(message, cipher, modulus):
    """D2 = log(message + N) / log(C)"""
    return Decimal(Decimal(math.log(message + modulus))/Decimal(math.log(cipher)))

def main():
    """# TODO: Describe this method here"""
    pk, sk = generate_keypair()

    print("e:   ", pk['e'])
    print("N:   ", pk['N'])
    print("d:   ", sk['d'])

    print()

    # TODO: separar entrada de 10 em 10 numeros
    message1 = 1234567890
    print("m:   ", message1)
    cipher = encryption(message1, pk['e'], pk['N'])
    print("c:   ", cipher)
    decripted = decryption(cipher, sk['d'], pk['N'])
    print("m:   ", decripted)

    print()

    message2 = 9876543210
    print("m2:  ", message2)
    sk_d2 = collision_finder(message2, cipher, pk['N'])
    print("d2:  ", sk_d2)
    decripted2 = decryption(cipher, sk_d2, pk['N'])
    print("m2:  ", decripted2)


if __name__ == '__main__':
    main()
