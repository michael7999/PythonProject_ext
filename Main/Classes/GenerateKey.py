from cryptography.fernet import Fernet

class KeyGenerator:
    def generate_key(self):
        key = Fernet.generate_key()
        return key

    def save_key_to_file(self, key, file_path):
        with open(file_path, "wb") as file:
            file.write(key)

    def generate_and_save_key(self, file_path):
        key = self.generate_key()
        self.save_key_to_file(key, file_path)
    
      # verwijder de key.txt file
    def clear_key_file(self):
        file_path = "Key.txt"
    
        with open(file_path, "w") as file:
                            file.truncate(0)
        

# Voorbeeldgebruik:
#key_generator = KeyGenerator()
#key_generator.generate_and_save_key("Key.txt")
