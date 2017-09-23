"""
Development file to implement a deniable encryption cryptosystem
"""

from .collision import collision_finder
from .keys import generate_keypair
from .rsa import decryption, encryption

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
