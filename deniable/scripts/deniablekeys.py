#! /usr/bin/env python
"""deniablekeys is a script generate RSA public and private keys"""

from __future__ import print_function
from deniable.keys import generate_keypair

def main():
    """Main entry point for script."""
    print(generate_keypair())

if __name__ == '__main__':
    main()
