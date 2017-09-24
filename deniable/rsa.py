"""RSA cryptosystem"""

from __future__ import division
import decimal
from Crypto.PublicKey import RSA

decimal.getcontext().prec = 20

def _get_public_key(key):
    """Returns exponencial and module attribute
    for given public 'key' in pem format"""
    keys = RSA.importKey(key)
    return (keys.e, keys.n)

def _get_secret_key(key):
    """Returns exponencial and module attribute
    for given private 'key' in pem format"""
    keys = RSA.importKey(key)
    return (keys.d, keys.n)

def encryption(mes, pub):
    """Encrypt message 'mes' using 'pub' public key."""
    exp, mod = _get_public_key(pub)
    return pow(mes, exp, mod)

def decryption(cipher, sec):
    """Decrypt cipher 'c' using 'sec' secret key"""
    exp, mod = _get_secret_key(sec)
    if exp < 10**20:
        return pow(cipher, exp, mod)

    exp = decimal.Decimal(exp/(10**20))
    return int(round((cipher**exp) % mod))
