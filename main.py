"""
Development file to implement a deniable encryption cryptosystem
"""

import sys
from deniable.collision import collision_finder
from deniable.rsa import decryption, encryption
from deniable.keys import generate_keypair

def main():
    """Do main stuffs (just for development)."""
    pub, sec = generate_keypair(22)

    print("e:   ", pub['e'])
    print("N:   ", pub['N'])
    print("d:   ", sec['d'])

    print()

    mes1 = 1234567890
    print("m:   ", mes1)
    cipher = encryption(mes1, pub['e'], pub['N'])
    print("c:   ", cipher)
    mesf1 = decryption(cipher, sec['d'], pub['N'])
    print("m:   ", mesf1)

    print()

    mes2 = 9876543210
    print("m2:  ", mes2)
    sk_d2 = collision_finder(mes2, cipher, pub['N'])
    print("d2:  ", sk_d2)
    mf2 = decryption(cipher, sk_d2, pub['N'])
    print("m2:  ", mf2)

if __name__ == '__main__':
    sys.exit(main())
