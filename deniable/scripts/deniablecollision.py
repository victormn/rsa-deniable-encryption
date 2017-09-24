#! /usr/bin/env python
"""deniablecollision is a script to find a private key such that a
given message can be decrypted from a given cipher using this private key."""

from __future__ import print_function
import argparse
from time import asctime, localtime, time
from logging import debug, basicConfig, DEBUG
from deniable.collision import collision_finder

def main():
    """Main entry point for script."""
    parser = argparse.ArgumentParser(
        description='Find a RSA private key collision.'
    )
    parser.add_argument(
        'cipher_path',
        help='Cipher',
    )
    parser.add_argument(
        'message_path',
        help='Message'
    )
    parser.add_argument(
        'publickey_path',
        help='Public Key in pem format'
    )
    parser.add_argument(
        '--log_path',
        type=str,
        help='Create a log in given path'
    )
    args = parser.parse_args()

    mfile = open(args.message_path, 'r')
    message = long(mfile.read())
    mfile.close()

    cfile = open(args.cipher_path, 'r')
    cipher = long(cfile.read())
    cfile.close()

    kfile = open(args.publickey_path, 'r')
    publickey = kfile.read()
    kfile.close()

    if args.log_path is not None:
        path = args.log_path + "/latency.log"
        basicConfig(filename=path, level=DEBUG)

    start = time()
    print(collision_finder(message, cipher, publickey))
    debug("%s: collision_finder: %s [s]", asctime(localtime(time())), time() - start)

if __name__ == '__main__':
    main()
