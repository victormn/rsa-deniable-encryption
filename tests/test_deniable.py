"""Tests for rsa.py and collision.py (with deniability)."""
from decimal import Decimal
from deniable.collision import collision_finder
from deniable.rsa import decryption

def test_collision_finder():
    """Can we properly use the collision finder?"""
    cipher = 10525764004464
    pub_n = 15771763372171

    mes1 = 9876543210
    sec_d = collision_finder(mes1, cipher, pub_n)
    assert sec_d == Decimal('1.0135075315253564751')

def test_decrypt_message_denied():
    """Can we properly decrypt a denied message?"""
    cipher = 10525764004464
    pub_n = 15771763372171

    sec_d = Decimal('1.0135075315253564751')
    mes = decryption(cipher, sec_d, pub_n)
    assert mes == 9876543210

def test_deny_message():
    """Can we properly deny a message?"""
    cipher = 10525764004464
    pub_n = 15771763372171

    mes1 = 9876543210
    sec_d = collision_finder(mes1, cipher, pub_n)
    mes2 = decryption(cipher, sec_d, pub_n)
    assert mes1 == mes2
