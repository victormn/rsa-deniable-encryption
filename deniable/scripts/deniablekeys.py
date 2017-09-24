#! /usr/bin/env python
"""deniablekeys is a script to generate RSA public and private keys"""

from __future__ import print_function
import argparse
from deniable.keys import generate_keypair

def main():
    """Main entry point for script."""
    parser = argparse.ArgumentParser(
        description='RSA keys generator.'
    )
    parser.add_argument(
        '-p',
        '--path',
        type=str,
        help='Path to save the keys',
    )
    args = parser.parse_args()
    if args.path is None:
        path = ""
    else:
        path = args.path + "/"

    keys = generate_keypair()

    pubf = open(path + 'publickey.pem', 'w')
    pubf.write(keys['pub'])
    pubf.close()

    secf = open(path + 'secretkey.pem', 'w')
    secf.write(keys['sec'])
    secf.close()

if __name__ == '__main__':
    main()
