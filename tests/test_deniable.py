"""Tests for rsa.py and collision.py (with deniability)."""

from deniable.collision import collision_finder
from deniable.rsa import decryption

def test_collision_finder():
    """Can we properly use the collision finder?"""
    cipher = 2648989795789
    sec = """-----BEGIN RSA PRIVATE KEY-----
MC8CAQACBgLLZ2vRwQIDAQABAgUOx3XPUQIDHAz3AgMZgQcCAwWnGwICfDsCAxe2
1g==
-----END RSA PRIVATE KEY-----"""
    mes1 = 9876543210
    sec_d = collision_finder(mes1, cipher, sec)
    assert sec_d == """-----BEGIN RSA PRIVATE KEY-----
MDQCAQACBgLLZ2vRwQIDAQABAgkFcyHNHnv+lsgCAxwM9wIDGYEHAgMRAioCAwci
uAIDF7bW
-----END RSA PRIVATE KEY-----"""

def test_decrypt_message_denied():
    """Can we properly decrypt a denied message?"""
    cipher = 2648989795789
    sec = """-----BEGIN RSA PRIVATE KEY-----
MDQCAQACBgLLZ2vRwQIDAQABAgkFcyHNHnv+lsgCAxwM9wIDGYEHAgMRAioCAwci
uAIDF7bW
-----END RSA PRIVATE KEY-----"""
    mes = decryption(cipher, sec)
    assert mes == 9876543210

def test_deny_message():
    """Can we properly deny a message?"""
    cipher = 2648989795789
    sec = """-----BEGIN RSA PRIVATE KEY-----
MC8CAQACBgLLZ2vRwQIDAQABAgUOx3XPUQIDHAz3AgMZgQcCAwWnGwICfDsCAxe2
1g==
-----END RSA PRIVATE KEY-----"""
    mes1 = 9876543210
    sec2 = collision_finder(mes1, cipher, sec)
    mes2 = decryption(cipher, sec2)
    assert mes1 == mes2
