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
    assert cipher == "002877160453915"

def test_decrypt_message():
    """Can we properly decrypt a message?"""
    sec = """-----BEGIN RSA PRIVATE KEY-----
MC8CAQACBgLLZ2vRwQIDAQABAgUOx3XPUQIDHAz3AgMZgQcCAwWnGwICfDsCAxe2
1g==
-----END RSA PRIVATE KEY-----"""
    cipher = "002877160453915"
    mes = decryption(cipher, sec)
    assert mes == "foo"

def test_cryptosystem():
    """Can we properly use the cryptosystem?"""
    keys = generate_keypair()
    (pub, sec) = (keys['pub'], keys['sec'])
    mes1 = """
    I'm taking over my body
    Back in control, no more shotty
    I bet a lot of me was lost
    "T"'s uncrossed and "I"'s undotted
    I fought it a lot and it seems a lot
    Like flesh is all I got
    Not any more, flesh out the door ?
    I must'a forgot, you can't trust me
    I'm open a moment and closed when you show it
    Before you know it I'm lost at sea
    And now that I write and think about it
    And the story unfolds
    You should take my life
    You should take my soul
    """
    cipher = encryption(mes1, pub)
    mes2 = decryption(cipher, sec)
    assert mes1 == mes2
