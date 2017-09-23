"""RSA cryptosystem"""

def encryption(mes, exp, mod):
    """Encrypt message 'mes' as follow:
    C = (mes ** exp) % mod."""

    return pow(mes, exp, mod)

def decryption(cipher, exp, mod):
    """Decrypt cipher c as follow:
    M = (cipher ** exp) % mod."""

    if exp == (exp//1):
        return pow(cipher, exp, mod)

    return round((cipher**exp) % mod)
