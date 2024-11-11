class DataStore:
    """ La clase sirve como un sistema de almacenamiento y utiliza el patrón de diseño 
    Estrategia para permitir el uso de diferentes algoritmos de cifrado, 
    ya que recibe una estrategia de cifrado como parámetro en su inicialización."""
    def __init__(self, cipher_strategy):
        self.cipher_strategy = cipher_strategy      #se implementa los métodos encrypt y decrypt
        self.data = {}

    # Agrega un registro
    def add_record(self, record_id, plaintext):
        encrypted = self.cipher_strategy.encrypt(plaintext)
        self.data[record_id] = encrypted

    # Recupera el registro  osea descifra
    def get_record(self, record_id):
        encrypted = self.data.get(record_id)
        if encrypted:
            return self.cipher_strategy.decrypt(encrypted)
        return None

    # Elimina el registro
    def delete_record(self, record_id):
        if record_id in self.data:
            del self.data[record_id]
