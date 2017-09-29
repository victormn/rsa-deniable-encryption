"""Find a private key such that a given message can be decrypted from a given cipher using RSA."""

import math
import sys
from time import asctime, localtime, time
from logging import debug, error
from decimal import Decimal, getcontext
from Crypto.PublicKey import RSA
from deniable.utils import slice_n, get_bytes

getcontext().prec = 20

def _get_key(key):
    """Returns a RSA key attribute
    for given 'key' in PEM format"""
    start = time()

    keys = RSA.importKey(key)
    dic_keys = {'e': "", 'd': "", 'n': ""}
    try:
        dic_keys = {'e': keys.e, 'd': keys.d, 'n': keys.n}
    except AttributeError:
        error("this key is not a private key")
        sys.exit()

    debug("%s: collision_finder: _get_key: %s [s]", asctime(localtime(time())), time() - start)
    return dic_keys

def _get_collision(mes, mod, cipher):
    """Returns a RSA key parameter D such that the message 'mes' can be decrypted from 'cipher'."""
    start = time()

    collision = Decimal(Decimal(math.log(mes + mod))/Decimal(math.log(cipher)))
    collision = int(collision*(10**20))

    debug("%s: collision_finder: collision: %s [s]", asctime(localtime(time())), time() - start)
    return str(collision)

def _generate_pem(collision, key):
    """Returns a PEM format for given keys attributes"""
    start = time()

    key = RSA.construct((key['n'], key['e'], key['d']))
    key.d = collision
    pem = "".join(map(chr, key.exportKey()))

    debug("%s: collision_finder: _generate_pem: %s [s]", asctime(localtime(time())), time() - start)
    return pem

def collision_finder(mes, cipher, pem):
    """Find RSA key parameter D such that the message 'mes' can be decrypted from 'cipher'."""
    key = _get_key(pem)
    s_cipher = slice_n(cipher, 15)
    s_mes = get_bytes(mes)

    i = 0
    collision = ""
    for piece in s_mes:
        try:
            collision += _get_collision(piece, key['n'], s_cipher[i])
        except IndexError:
            error("the second message length must be less than encripted message length")
            sys.exit()
        i += 1
    return _generate_pem(int(collision), key)
