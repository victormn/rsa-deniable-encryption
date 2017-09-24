"""RSA cryptosystem"""

from __future__ import division
import decimal
from time import asctime, localtime, time
from logging import debug
from Crypto.PublicKey import RSA

decimal.getcontext().prec = 20

def _get_bytes(string):
    """Returns a integer that represents the bytes array of a given string"""
    start = time()

    str_bytes = list(str.encode(string))
    aux = ""
    for byte in str_bytes:
        aux += "%03d" % (byte,)
    num = int(aux)

    debug("%s: rsa: _get_bytes: %s [s]", asctime(localtime(time())), time() - start)
    return num

def _get_string(num):
    """Resturns a string that can be represented as the bytes array of a given num"""
    start = time()

    str_num = str(num)
    if len(str_num) % 3 is not 0:
        str_num = "0" + str_num
    i = 0
    aux = ""
    bytes_list = list()
    for char in str_num:
        aux += char
        i += 1
        if i == 3:
            bytes_list.append(int(aux))
            i = 0
            aux = ""
    decoded = "".join(map(chr, bytes_list))

    debug("%s: rsa: _get_string: %s [s]", asctime(localtime(time())), time() - start)
    return decoded

def _get_public_key(key):
    """Returns exponencial and module attribute
    for given public 'key' in pem format"""
    start = time()

    keys = RSA.importKey(key)
    pub = (keys.e, keys.n)

    debug("%s: rsa: _get_public_key: %s [s]", asctime(localtime(time())), time() - start)
    return pub

def _get_secret_key(key):
    """Returns exponencial and module attribute
    for given private 'key' in pem format"""
    start = time()

    keys = RSA.importKey(key)
    sec = (keys.d, keys.n)

    debug("%s: rsa: _get_secret_key: %s [s]", asctime(localtime(time())), time() - start)
    return sec

def encryption(mes, pub):
    """Encrypt message 'mes' using 'pub' public key."""
    exp, mod = _get_public_key(pub)
    return pow(_get_bytes(mes), exp, mod)

def decryption(cipher, sec):
    """Decrypt cipher 'c' using 'sec' secret key"""
    exp, mod = _get_secret_key(sec)
    if exp < 10**20:
        num = pow(int(cipher), exp, mod)
        return _get_string(num)

    exp = decimal.Decimal(exp/(10**20))
    num = int(round((int(cipher)**exp) % mod))
    return _get_string(num)
