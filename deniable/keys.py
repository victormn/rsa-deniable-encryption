"""Defines RSA public and private keys"""

import random
import functools

def _gcd(*numbers):
    """Return the greatest common divisor from numbers."""
    from fractions import gcd
    return functools.reduce(gcd, numbers)

def _lcm(*numbers):
    """Return the least common multiple from numbers."""
    def lcm(num1, num2):
        """Return the least common multiple from two numbers."""
        return (num1 * num2) // _gcd(num1, num2)
    return functools.reduce(lcm, numbers, 1)

def _multiplicative_inverse(exp, phi):
    """Return a multiplicative inverse of e mod phi."""
    aux1 = 0
    aux2 = 1
    old = phi
    while phi != 0:
        aux3 = exp // phi
        (exp, phi) = (phi, exp % phi)
        (aux1, aux2) = ((aux2 - (aux3 * aux1)), aux1)

    if aux2 < 0:
        aux2 = aux2 + old

    return aux2

def _create_sieve(num):
    """Return all primes <= num."""
    np1 = num + 1
    sli = list(range(np1))
    sli[1] = 0
    sqrtn = int(round(num**0.5))
    for i in range(2, sqrtn + 1):
        if sli[i]:
            sli[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, sli)

def _rand_prime(size, sieve):
    """Return a random prime >= size using a sieve set."""
    rand = random.randrange(2**(size-2), 2**size)
    while not rand in sieve:
        rand += 1
    return rand

def generate_keypair(size):
    """Generates RSA public and private key."""
    sieve = set(_create_sieve(2**size))
    pk_p = _rand_prime(size, sieve)
    pk_q = _rand_prime(size, sieve)

    if pk_p > pk_q:
        (pk_p, pk_q) = (pk_q, pk_p)

    pk_n = pk_p * pk_q
    phi = _lcm((pk_p-1), (pk_q-1))
    pk_e = 65537
    pk_g = _gcd(pk_e, phi)
    while pk_g != 1:
        pk_e = random.randrange(1, phi)
        pk_g = _gcd(pk_e, phi)

    sk_d = _multiplicative_inverse(pk_e, phi)
    return ({'e': pk_e, 'N': pk_n}, {'d': sk_d, 'N': pk_n})
