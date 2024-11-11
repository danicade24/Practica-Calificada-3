from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class RSACipher:
    def __init__(self, public_key, private_key=None):
        self.public_key = public_key
        self.private_key = private_key

    def encrypt(self, message):
        cipher = PKCS1_OAEP.new(self.public_key)
        return cipher.encrypt(message.encode())

    def decrypt(self, encrypted_data):
        cipher = PKCS1_OAEP.new(self.private_key)
        return cipher.decrypt(encrypted_data).decode()
