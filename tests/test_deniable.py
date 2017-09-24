"""Tests for rsa.py and collision.py (with deniability)."""

from deniable.collision import collision_finder
from deniable.rsa import decryption

def test_collision_finder():
    """Can we properly use the collision finder?"""
    cipher = "7928186168759"
    sec = """-----BEGIN RSA PRIVATE KEY-----
MDECAQACBghK5FNUlwIDAQABAgYCIgDwCMECAyqx9QIDMbjbAgMWsskCAwX2/QID
D3n/
-----END RSA PRIVATE KEY-----"""
    mes1 = "bar"
    sec_d = collision_finder(mes1, cipher, sec)
    assert sec_d == """-----BEGIN RSA PRIVATE KEY-----
MDQCAQACBghK5FNUlwIDAQABAgkFck+wk/ieerACAyqx9QIDMbjbAgMkY0QCAypP
7gIDD3n/
-----END RSA PRIVATE KEY-----"""

def test_decrypt_message_denied():
    """Can we properly decrypt a denied message?"""
    cipher = "7928186168759"
    sec = """-----BEGIN RSA PRIVATE KEY-----
MDQCAQACBghK5FNUlwIDAQABAgkFck+wk/ieerACAyqx9QIDMbjbAgMkY0QCAypP
7gIDD3n/
-----END RSA PRIVATE KEY-----"""
    mes = decryption(cipher, sec)
    assert mes == "bar"

def test_deny_message():
    """Can we properly deny a message?"""
    cipher = "3418934743560"
    sec = """-----BEGIN RSA PRIVATE KEY-----
MDECAQACBghK5FNUlwIDAQABAgYCIgDwCMECAyqx9QIDMbjbAgMWsskCAwX2/QID
D3n/
-----END RSA PRIVATE KEY-----"""
    mes1 = "2 1"
    sec2 = collision_finder(mes1, cipher, sec)
    mes2 = decryption(cipher, sec2)
    assert mes1 == mes2
