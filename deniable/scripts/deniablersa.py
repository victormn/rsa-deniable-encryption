#! /usr/bin/env python
"""deniablersa is a script to encryption and decryption using RSA cryptosystem"""

from __future__ import print_function
import argparse
from time import asctime, localtime, time
from logging import debug, basicConfig, DEBUG
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
    parser.add_argument(
        '--log_path',
        type=str,
        help='Create a log in given path'
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

    if args.log_path is not None:
        path = args.log_path + "/latency.log"
        basicConfig(filename=path, level=DEBUG)

    start = time()
    kfile = open(args.key_path, 'r')
    key = kfile.read()
    kfile.close()
    debug("%s: rsa: open key file: %s [s]", asctime(localtime(time())), time() - start)

    if args.enc:
        start = time()
        print(encryption(message, key))
        debug("%s: rsa: encryption: %s [s]", asctime(localtime(time())), time() - start)
    elif args.dec:
        start = time()
        print(decryption(message, key))
        debug("%s: rsa: decryption: %s [s]", asctime(localtime(time())), time() - start)
    else:
        print("Use --enc to encrypt a given message or --dec to decrypt")

if __name__ == '__main__':
    main()
