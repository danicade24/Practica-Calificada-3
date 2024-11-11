import unittest
from unittest.mock import patch
from src.Ejercicio1_Parte1.key_generator import KeyGenerator

class FakeRSAKey:
    """Fake class para simular un objeto de clave RSA"""
    def __init__(self, size):
        self.size = size

    def publickey(self):
        return FakeRSAKey(self.size)

    def export_key(self):
        return b"fake_key_data"

    def size_in_bits(self):
        return self.size

class TestKeyGenerator(unittest.TestCase):
    def setUp(self):
        self.key_size = 2048
        self.key_generator = KeyGenerator(key_size=self.key_size)

    @patch('src.Ejercicio1_Parte1.key_generator.RSA.generate')
    def test_generate_keys(self, mock_generate):
        # Configurar el mock para que devuelva una clave fake
        mock_generate.return_value = FakeRSAKey(self.key_size)

        private_key, public_key = self.key_generator.generate_keys()
        
        # Verificar que el mock fue llamado con el tamaño correcto
        mock_generate.assert_called_once_with(self.key_size)
        
        # Verificar que los valores devueltos son instancias de FakeRSAKey
        self.assertIsInstance(private_key, FakeRSAKey)
        self.assertIsInstance(public_key, FakeRSAKey)

        # Verificar que el tamaño de la clave es el esperado
        self.assertEqual(private_key.size_in_bits(), self.key_size)
        self.assertEqual(public_key.size_in_bits(), self.key_size)

    @patch('src.Ejercicio1_Parte1.key_generator.RSA.generate')
    def test_serialize_private_key(self, mock_generate):
        # Configurar el mock para que devuelva una clave privada fake
        mock_generate.return_value = FakeRSAKey(self.key_size)
        
        private_key, _ = self.key_generator.generate_keys()
        serialized_private_key = self.key_generator.serialize_private_key(private_key)
        
        # Comprobar que el resultado es el valor fake esperado
        self.assertEqual(serialized_private_key, b"fake_key_data")

    @patch('src.Ejercicio1_Parte1.key_generator.RSA.generate')
    def test_serialize_public_key(self, mock_generate):
        # Configurar el mock para que devuelva una clave pública fake
        mock_generate.return_value = FakeRSAKey(self.key_size)
        
        _, public_key = self.key_generator.generate_keys()
        serialized_public_key = self.key_generator.serialize_public_key(public_key)
        
        # Comprobar que el resultado es el valor fake esperado
        self.assertEqual(serialized_public_key, b"fake_key_data")

    def test_invalid_key_size(self):
        """Probar que un tamaño de clave no es válido"""
        with self.assertRaises(ValueError):
            KeyGenerator(key_size=512)

if __name__ == '__main__':
    unittest.main()
