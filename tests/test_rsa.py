"""Tests for rsa.py and keys.py."""
from deniable.rsa import decryption, encryption
from deniable.keys import generate_keypair

def test_encrypt_message():
    """Can we properly encrypt a message?"""
    pub = {'e': 65537, 'N': 15771763372171}

    mes = 1234567890
    cipher = encryption(mes, pub['e'], pub['N'])
    assert cipher == 10525764004464

def test_decrypt_message():
    """Can we properly decrypt a message?"""
    sec = {'d': 7121439591425, 'N': 15771763372171}

    cipher = 10525764004464
    mes = decryption(cipher, sec['d'], sec['N'])
    assert mes == 1234567890

def test_cryptosystem():
    """Can we properly use the cryptosystem?"""
    pub, sec = generate_keypair()

    mes1 = 1234567890
    cipher = encryption(mes1, pub['e'], pub['N'])
    mes2 = decryption(cipher, sec['d'], sec['N'])
    assert mes1 == mes2
