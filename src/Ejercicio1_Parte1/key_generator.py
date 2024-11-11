from Crypto.PublicKey import RSA  

class KeyGenerator:  
    def __init__(self, key_size: int):  
        """Inicializa el generador con el tamaño de clave especificado.  
        key_size: El tamaño de la clave puede ser ajustado a 1024 o 2048.  
        """  
        if key_size not in (1024, 2048):  
            raise ValueError("El tamaño de la clave debe ser 1024 o 2048 bits.")  
        self.key_size = key_size  

    def generate_keys(self):  
        """Genera y devuelve un par de clave RSA""" 
        if self.key_size not in (1024, 2048):
            raise ValueError("El tamaño de la clave debe ser 1024 o 2048 bits.") 
        key = RSA.generate(self.key_size)  
        return key, key.publickey()  
    
    def serialize_private_key(self, private_key):  
        """Serializa la clave privada"""  
        return private_key.export_key()  
    
    def serialize_public_key(self, public_key):  
        """Serializa la clave pública"""  
        return public_key.export_key()
    