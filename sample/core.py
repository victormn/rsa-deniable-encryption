import math
import random
from functools import reduce
from decimal import *
getcontext().prec = 50

def gcd(*numbers):
    from fractions import gcd
    return reduce(gcd, numbers)

def lcm(*numbers):
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)

def multiplicative_inverse(e, phi):
    x = 0
    lx = 1
    oldPhi = phi
    while phi != 0:
        q = e // phi
        (e, phi) = (phi, e % phi)
        (x, lx) = ((lx - (q * x)), x)
   
    if lx < 0:
        lx = lx + oldPhi

    return lx

def generate_keypair(p, q):
    n = p * q
    phi = lcm((p-1), (q-1))
    e = 65537
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)  
    return ((e, n), (d, n))

def encryption(e, N, m):
    return pow(m, e, N)

def decryption(d, N, c):
    if d == (d//1):
        return pow(c, d, N)
    else:
        return round((c**d) % N)
        
def collisionFinder(m2, C, N):
    """D2 = log(M2 + N) / log(C)"""
    return Decimal(math.log(m2 + N))/Decimal(math.log(C))

def main():
    p = 104723
    q = 104729
    public, private = generate_keypair(p, q)

    e = public[0]
    N = public[1]
    d = private[0]

    print("e:   ", e)
    print("N:   ", N)
    print("d:   ", d)

    print()

    m = 9965465490
    print("m:   ", m)
    c = encryption(e, N, m)
    print("c:   ", c)
    mf = decryption(d, N, c)
    print("mf:  ", mf)


    print()

    m2 = 878974658
    print("m2:  ", m2)
    d2 = collisionFinder(m2, c, N)
    print("d2:  ", d2)
    mf2 = decryption(d2, N, c)
    print("mf2: ", mf2)


if __name__ == '__main__':
    main()