import math
import decimal

decimal.getcontext().prec = 20

def collision_finder(m2, c, N):
    """Find a RSA key parameter D such that the message m2 can be decrypted from cipher c
    D2 = log(m2 + N) / log(C)."""
    
    return decimal.Decimal(decimal.Decimal(math.log(m2 + N))/decimal.Decimal(math.log(c)))
