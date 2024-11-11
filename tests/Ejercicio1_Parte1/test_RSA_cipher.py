import unittest
from unittest.mock import patch
from src.Ejercicio1_Parte1.key_generator import KeyGenerator
from src.Ejercicio1_Parte1.RSA_cipher import RSACipher

class TestRSACipher(unittest.TestCase):

    def setUp(self):
        key_gen = KeyGenerator(key_size=2048)
        private_key, public_key = key_gen.generate_keys()
        self.encryptor = RSACipher(public_key, private_key)

    def test_encrypt_decrypt(self):
        message = "Buenas tardes"
        encrypted_message = self.encryptor.encrypt(message)
        self.assertIsInstance(encrypted_message, bytes)
        
        decrypted_message = self.encryptor.decrypt(encrypted_message)
        self.assertEqual(decrypted_message, message)

    def test_encrypt_too_long_message(self):  
        long_message = "A" * (self.encryptor.get_max_message_length() + 1)  # Un mensaje demasiado largo  
        with self.assertRaises(ValueError) as context:  
            self.encryptor.encrypt(long_message)  
        self.assertEqual(str(context.exception), "Mensaje es muy largo")  
            
    def test_decrypt_invalid_data(self):  
        invalid_data = b'no es un mensaje cifrado valido'  
        with self.assertRaises(Exception) as context:  
            self.encryptor.decrypt(invalid_data)  
        self.assertTrue("Error durante el descifrado" in str(context.exception)) 
    
    # Uso de mocks para reemplazar el método de cifrado que lanza una excepción. Esto simula que hubo un fallo en el proceso de cifrado.
    @patch("src.Ejercicio1_Parte1.RSA_cipher.PKCS1_OAEP.new")
    def test_encrypt_raises_exception(self, mock_cipher):
        # Configurar el mock para que lance una excepción
        mock_cipher.side_effect = Exception("Error de cifrado simulado")
        message = "Mensaje de prueba"

        with self.assertRaises(Exception) as context:
            self.encryptor.encrypt(message)

        self.assertTrue("Error durante el cifrado" in str(context.exception))

if __name__ == '__main__':
    unittest.main()
