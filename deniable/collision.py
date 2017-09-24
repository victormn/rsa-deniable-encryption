"""Find a private key such that a given message can be decrypted from a given cipher using RSA."""

import math
from time import asctime, localtime, time
from logging import debug
from decimal import Decimal, getcontext
from Crypto.PublicKey import RSA

getcontext().prec = 20

def _get_key(key):
    """Returns a RSA key attribute
    for given 'key' in PEM format"""
    start = time()

    keys = RSA.importKey(key)
    dic_keys = {'e': keys.e, 'd': keys.d, 'n': keys.n}

    debug("%s: collision_finder: _get_key: %s [s]", asctime(localtime(time())), time() - start)
    return dic_keys

def _get_collision(mes, mod, cipher):
    """Returns a RSA key parameter D such that the message 'mes' can be decrypted from 'cipher'."""
    start = time()

    collision = Decimal(Decimal(math.log(mes + mod))/Decimal(math.log(cipher)))

    debug("%s: collision_finder: collision: %s [s]", asctime(localtime(time())), time() - start)
    return collision

def _generate_pem(collision, key):
    """Returns a PEM format for given keys attributes"""
    start = time()

    key = RSA.construct((long(key['n']), long(key['e']), key['d']))
    key.d = collision*(10**20)
    pem = key.exportKey()

    debug("%s: collision_finder: _generate_pem: %s [s]", asctime(localtime(time())), time() - start)
    return pem

def collision_finder(mes, cipher, pem):
    """Find RSA key parameter D such that the message 'mes' can be decrypted from 'cipher'."""
    key = _get_key(pem)
    collision = _get_collision(mes, key['n'], cipher)
    return _generate_pem(collision, key)
