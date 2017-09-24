"""Find a private key such that a given message can be decrypted from a given cipher using RSA."""

import math
from decimal import Decimal, getcontext
from Crypto.PublicKey import RSA

getcontext().prec = 20

def _get_key(key):
    """Returns a RSA key attribute
    for given 'key' in PEM format"""
    keys = RSA.importKey(key)
    return {'e': keys.e, 'd': keys.d, 'n': keys.n}

def _generate_pem(collision, key):
    """Returns a PEM format for given keys attributes"""
    key = RSA.construct((long(key['n']), long(key['e']), key['d']))
    key.d = collision*(10**20)
    return key.exportKey()

def collision_finder(mes, cipher, pem):
    """Find RSA key parameter D such that the message 'mes' can be decrypted from 'cipher'."""
    key = _get_key(pem)
    collision = Decimal(Decimal(math.log(mes + key['n']))/Decimal(math.log(cipher)))
    return _generate_pem(collision, key)
