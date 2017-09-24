#! /usr/bin/env python
"""deniablekeys is a script to generate RSA public and private keys"""

from __future__ import print_function
import argparse
from time import asctime, localtime, time
from logging import debug, basicConfig, DEBUG
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
    parser.add_argument(
        '--log_path',
        type=str,
        help='Create a log in given path'
    )
    args = parser.parse_args()
    if args.path is None:
        path = ""
    else:
        path = args.path + "/"

    if args.log_path is not None:
        log_path = args.log_path + "/latency.log"
        basicConfig(filename=log_path, level=DEBUG)

    start = time()
    keys = generate_keypair()
    debug("%s: keys: %s [s]", asctime(localtime(time())), time() - start)

    start = time()
    pubf = open(path + 'publickey.pem', 'w')
    pubf.write(keys['pub'])
    pubf.close()
    debug("%s: keys: save publickey: %s [s]", asctime(localtime(time())), time() - start)

    start = time()
    secf = open(path + 'secretkey.pem', 'w')
    secf.write(keys['sec'])
    secf.close()
    debug("%s: keys: save secretkey: %s [s]", asctime(localtime(time())), time() - start)

if __name__ == '__main__':
    main()
