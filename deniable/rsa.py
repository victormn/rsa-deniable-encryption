"""RSA cryptosystem"""

from __future__ import division
import decimal
from time import asctime, localtime, time
from logging import debug
from Crypto.PublicKey import RSA

decimal.getcontext().prec = 20

def _slice(string, size):
    """Given a string, returns a slice array of int such that each element has size 'size'."""
    start = time()

    i = 0
    aux = ""
    result = list()
    for char in string:
        aux += char
        i += 1
        if i == size:
            result.append(int(aux))
            i = 0
            aux = ""

    if i > 0:
        result.append(int(aux))

    debug("%s: rsa: _slice: %s [s]", asctime(localtime(time())), time() - start)
    return result

def _get_bytes(string):
    """Returns a integer that represents the bytes array of a given string"""
    start = time()

    str_bytes = list(str.encode(string))
    aux = ""
    for byte in str_bytes:
        aux += "%03d" % (byte,)

    debug("%s: rsa: _get_bytes: %s [s]", asctime(localtime(time())), time() - start)
    return aux

def _get_string(str_num):
    """Resturns a string that can be represented as the bytes array of a given num"""
    start = time()

    if len(str_num) % 3 is not 0:
        str_num = "0"*(3 - (len(str_num) % 3)) + str_num

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

def _trim(num):
    string = str(num)
    if len(string) <= 3:
        return "%03d" % (num,)
    if len(string) <= 6:
        return "%06d" % (num,)

    return "%09d" % (num,)

def encryption(mes, pub):
    """Encrypt message 'mes' using 'pub' public key."""
    exp, mod = _get_public_key(pub)
    sliced = _slice(_get_bytes(mes), 9)
    aux = ""
    for piece in sliced:
        aux += "%015d" % (pow(piece, exp, mod),)
    return aux

def decryption(cipher, sec):
    """Decrypt cipher 'c' using 'sec' secret key"""
    exp, mod = _get_secret_key(sec)
    sliced = _slice(cipher, 15)
    aux = ""
    if exp < 10**20:
        for piece in sliced:
            aux += _trim(pow(piece, exp, mod))
        return _get_string(aux)

    exp_sliced = _slice(str(exp), 30)
    i = 0
    for piece in sliced:
        exp_current = decimal.Decimal(exp_sliced[i]/(10**20))
        aux += str(int(round((piece**exp_current) % mod)))
        i += 1
    return _get_string(aux)
