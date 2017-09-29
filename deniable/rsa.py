"""RSA cryptosystem"""

from __future__ import division
import decimal
import sys
from time import asctime, localtime, time
from logging import debug, error
from Crypto.PublicKey import RSA
from deniable.utils import get_bytes, get_string, slice_n, trim

decimal.getcontext().prec = 20

def _get_public_key(key):
    """Returns exponencial and module attribute
    for given public 'key' in pem format"""
    start = time()

    keys = RSA.importKey(key)
    pub = ("", "")
    try:
        pub = (keys.e, keys.n)
    except AttributeError:
        error("this key is not a valid key")
        sys.exit()

    debug("%s: rsa: _get_public_key: %s [s]", asctime(localtime(time())), time() - start)
    return pub

def _get_secret_key(key):
    """Returns exponencial and module attribute
    for given private 'key' in pem format"""
    start = time()

    keys = RSA.importKey(key)
    sec = ("", "")
    try:
        sec = (keys.d, keys.n)
    except AttributeError:
        error("this key is not a private key")
        sys.exit()

    debug("%s: rsa: _get_secret_key: %s [s]", asctime(localtime(time())), time() - start)
    return sec

def encryption(mes, pub):
    """Encrypt message 'mes' using 'pub' public key."""
    exp, mod = _get_public_key(pub)
    sliced = get_bytes(mes)
    aux = ""
    for piece in sliced:
        aux += "%015d" % (pow(piece, exp, mod),)
    return aux

def decryption(cipher, sec):
    """Decrypt cipher 'c' using 'sec' secret key"""
    exp, mod = _get_secret_key(sec)
    sliced = slice_n(cipher, 15)
    aux = ""
    if exp < 10**20:
        i = 0
        while i < (len(sliced)-1):
            aux += "%09d" % (pow(sliced[i], exp, mod),)
            i += 1
        aux += trim(pow(sliced[i], exp, mod))
        return get_string(aux)

    exp_sliced = slice_n(str(exp), 21)
    i = 0
    for piece in exp_sliced:
        exp_current = decimal.Decimal(piece/(10**20))
        try:
            aux += trim(int(round((sliced[i]**exp_current) % mod)))
        except IndexError:
            error("wrong private key")
            sys.exit()
        i += 1
    return get_string(aux)
