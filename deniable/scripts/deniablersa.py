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
        'key_path',
        type=str,
        help='Path to a RSA public/private key in PEM format',
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

    kfile = open(args.key_path, 'r')
    key = kfile.read()
    kfile.close()

    if args.enc:
        print(encryption(message, key))
    elif args.dec:
        print(decryption(message, key))
    else:
        print("Use --enc to encrypt a given message or --dec to decrypt")

if __name__ == '__main__':
    main()
