from utilitiespackage.crypto import aes_encrypt, aes_decrypt


def test_aes_encrypt():
    assert aes_decrypt(aes_encrypt("plaintext", "password"), "password") == b"plaintext"
