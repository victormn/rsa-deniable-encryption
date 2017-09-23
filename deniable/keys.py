import random
import functools

def _gcd(*numbers):
    """Return the greatest common divisor from numbers."""
    from fractions import gcd
    return functools.reduce(gcd, numbers)

def _lcm(*numbers):
    """Return the least common multiple from numbers."""
    def lcm(a, b):
        return (a * b) // _gcd(a, b)
    return functools.reduce(lcm, numbers, 1)

def _multiplicative_inverse(e, phi):
    """Return a multiplicative inverse of e mod phi."""
    x = 0
    y = 1
    old = phi
    while phi != 0:
        q = e // phi
        (e, phi) = (phi, e % phi)
        (x, y) = ((y - (q * x)), x)

    if y < 0:
        y = y + old

    return y

def _create_sieve(n):
    """Return all primes <= n."""
    np1 = n + 1
    s = list(range(np1)) 
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)

def _rand_prime(size, sieve):
    """Return a random prime >= size using a sieve set."""
    rand = random.randrange(2**(size-2), 2**size)
    while not rand in sieve:
        rand += 1
    return rand

def generate_keypair(size):
    """Generates RSA public and private key."""
    sieve = set(_create_sieve(2**size))
    p = _rand_prime(size, sieve)
    q = _rand_prime(size, sieve)

    if p > q:
        (p, q) = (q, p)

    n = p * q
    phi = _lcm((p-1), (q-1))
    e = 65537
    g = _gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = _gcd(e, phi)

    d = _multiplicative_inverse(e, phi)
    return ({'e': e, 'N': n}, {'d': d, 'N': n})