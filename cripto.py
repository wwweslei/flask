from simple_aes_cipher import AESCipher, generate_secret_key
from os import environ


def encrypt_text(raw_text):
    cipher = AESCipher(generate_secret_key(environ.get("SECRET_KEY")))
    return cipher.encrypt(raw_text)


def decrypt_text(encrypt_text):
    cipher = AESCipher(generate_secret_key(environ.get("SECRET_KEY")))
    return cipher.decrypt(encrypt_text)
