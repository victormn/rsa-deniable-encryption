#! /usr/bin/env python
"""deniablersa is a script to encryption and decryption using RSA cryptosystem"""

from __future__ import print_function
import argparse
from deniable.rsa import decryption, encryption

def main():
    """Main entry point for script."""
    parser = argparse.ArgumentParser(
        description='RSA cryptosystem.'
    )
    parser.add_argument(
        'exp',
        type=float,
        help='RSA public/private key (E/D)',
    )
    parser.add_argument(
        'mod',
        type=int,
        help='RSA public/private key (N)'
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-e',
        '--enc',
        help='Encrypt a given input message',
        action="store_true",
    )
    group.add_argument(
        '-d',
        '--dec',
        help='Decrypt a given input cipher',
        action="store_true",
    )

    args = parser.parse_args()
    message = input()
    if message == "":
        print('Error: Input a valid message, please.')
        return

    if args.enc:
        print(encryption(message, args.exp, args.mod))
    elif args.dec:
        print(decryption(message, args.exp, args.mod))
    else:
        print("Use --enc to encrypt a given message or --dec to decrypt")

if __name__ == '__main__':
    main()
