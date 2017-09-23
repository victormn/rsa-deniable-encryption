"""Find a private key such that a given message can be decrypted from a given cipher using RSA."""

import math
import decimal

decimal.getcontext().prec = 20

def collision_finder(mes, cipher, mod):
    """Find RSA key parameter D such that the message 'mes' can be decrypted from 'cipher'."""
    return decimal.Decimal(decimal.Decimal(math.log(mes + mod))/decimal.Decimal(math.log(cipher)))
