"""Tests for rsa.py and keys.py."""

from deniable.rsa import decryption, encryption
from deniable.keys import generate_keypair

def test_encrypt_message():
    """Can we properly encrypt a message?"""
    pub = """-----BEGIN PUBLIC KEY-----
MCEwDQYJKoZIhvcNAQEBBQADEAAwDQIGAstna9HBAgMBAAE=
-----END PUBLIC KEY-----"""
    mes = "foo"
    cipher = encryption(mes, pub)
    assert cipher == 2877160453915

def test_decrypt_message():
    """Can we properly decrypt a message?"""
    sec = """-----BEGIN RSA PRIVATE KEY-----
MC8CAQACBgLLZ2vRwQIDAQABAgUOx3XPUQIDHAz3AgMZgQcCAwWnGwICfDsCAxe2
1g==
-----END RSA PRIVATE KEY-----"""
    cipher = "2877160453915"
    mes = decryption(cipher, sec)
    assert mes == "foo"

def test_cryptosystem():
    """Can we properly use the cryptosystem?"""
    keys = generate_keypair()
    (pub, sec) = (keys['pub'], keys['sec'])
    mes1 = "1 2"
    cipher = encryption(mes1, pub)
    mes2 = decryption(cipher, sec)
    assert mes1 == mes2
