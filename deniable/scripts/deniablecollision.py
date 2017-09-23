#! /usr/bin/env python
"""deniablecollision is a script to Find a private key such that a
given message can be decrypted from a given cipher using RSA public key."""

from __future__ import print_function
import argparse
from deniable.collision import collision_finder

def main():
    """Main entry point for script."""
    parser = argparse.ArgumentParser(
        description='RSA cryptosystem.'
    )
    parser.add_argument(
        'cipher',
        type=float,
        help='Cipher',
    )
    parser.add_argument(
        'message',
        type=int,
        help='Message'
    )
    parser.add_argument(
        'publicKey',
        type=int,
        help='Public Key'
    )
    args = parser.parse_args()

    print(collision_finder(args.message, args.cipher, args.publicKey))

if __name__ == '__main__':
    main()
