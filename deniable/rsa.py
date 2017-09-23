def encryption(m, e, N):
    """Encrypt message m as follow:
    C = (m ** e) mod N."""

    return pow(m, e, N)

def decryption(c, d, N):
    """Decrypt cipher c as follow:
    M = (c ** d) % N."""

    if d == (d//1):
        return pow(c, d, N)

    return round((c**d) % N)
