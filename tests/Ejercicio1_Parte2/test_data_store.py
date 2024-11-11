import unittest
from unittest.mock import Mock
from src.Ejercicio1_Parte2.data_store import DataStore

class TestDataStore(unittest.TestCase):

    def setUp(self):
        # Creamos un mock de cipher_strategy
        self.mock_cipher_strategy = Mock()
        # Configuramos el mock para que devuelva valores específicos al cifrar y descifrar
        self.mock_cipher_strategy.encrypt.return_value = b"encrypted_data"
        self.mock_cipher_strategy.decrypt.return_value = "decrypted_data"
        
        # Inicializamos DataStore con el mock de cipher_strategy
        self.data_store = DataStore(cipher_strategy=self.mock_cipher_strategy)

    def test_add_record(self):
        # Agregar un registro
        self.data_store.add_record("record1", "plaintext_data")
        
        # Verificar que el método encrypt fue llamado una vez con el argumento "plaintext_data"
        self.mock_cipher_strategy.encrypt.assert_called_once_with("plaintext_data")
        
        # Comprobar que el registro se guardó cifrado en data_store.data
        self.assertEqual(self.data_store.data["record1"], b"encrypted_data")

    def test_get_record(self):
        # Agregar un registro para luego recuperarlo
        self.data_store.data["record1"] = b"encrypted_data"
        
        # Recuperar el registro
        result = self.data_store.get_record("record1")
        
        # Verificar que el método decrypt fue llamado una vez con el argumento b"encrypted_data"
        self.mock_cipher_strategy.decrypt.assert_called_once_with(b"encrypted_data")
        
        # Comprobar que el resultado es el valor descifrado
        self.assertEqual(result, "decrypted_data")

    def test_get_record_not_found(self):
        # Intentar recuperar un registro que no existe
        result = self.data_store.get_record("non_existing_record")
        
        # Comprobar que el resultado es None
        self.assertIsNone(result)

    def test_delete_record(self):
        # Agregar un registro para luego eliminarlo
        self.data_store.data["record1"] = b"encrypted_data"
        
        # Eliminar el registro
        self.data_store.delete_record("record1")
        
        # Verificar que el registro fue eliminado de data_store.data
        self.assertNotIn("record1", self.data_store.data)

    def test_delete_record_not_found(self):
        # Intentar eliminar un registro que no existe
        # Esto no debe lanzar ningún error
        try:
            self.data_store.delete_record("non_existing_record")
        except Exception as e:
            self.fail(f"delete_record raised an exception unexpectedly: {e}")

if __name__ == '__main__':
    unittest.main()
