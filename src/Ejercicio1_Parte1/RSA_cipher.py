from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import hashlib

class RSACipher:
    def __init__(self, public_key: RSA.RsaKey, private_key: RSA.RsaKey):
        self.public_key = public_key
        self.private_key = private_key

    def encrypt(self, message: str) -> bytes:
        """Cifra un mensaje de texto plano utilizando la clave pública"""
        # Validar la longitud del mensaje antes de cifrar
        self._validate_message_length(message)
        
        try:
            cipher = PKCS1_OAEP.new(self.public_key)
            encrypted_message = cipher.encrypt(message.encode())
            return encrypted_message
        except Exception as e:
            raise Exception(f"Error durante el cifrado: {e}")

    def decrypt(self, encrypted_message: bytes) -> str:
        """Descifra un mensaje cifrado utilizando la clave privada"""
        try:
            cipher = PKCS1_OAEP.new(self.private_key)
            decrypted_message = cipher.decrypt(encrypted_message)
            return decrypted_message.decode()
        except Exception as e:
            raise Exception(f"Error durante el descifrado: {e}")

    def _validate_message_length(self, message: str):
        max_length = self.get_max_message_length()
        if len(message.encode()) > max_length:
            raise ValueError("Mensaje es muy largo")

    def get_max_message_length(self) -> int:
        # Tamaño de la clave en bytes
        key_size_bytes = self.public_key.size_in_bytes()
        # Tamaño del hash (SHA-256)
        hash_length = hashlib.sha256().digest_size
        
        # Calcular la longitud máxima del mensaje que se puede cifrar
        return key_size_bytes - 2 * hash_length - 2
