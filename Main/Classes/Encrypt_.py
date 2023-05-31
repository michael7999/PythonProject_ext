import os
from cryptography.fernet import Fernet

class FileEncryptor:
    def __init__(self, key_file_path):
        self.key = self.load_key_from_file(key_file_path)

    def load_key_from_file(self, file_path):
        with open(file_path, "rb") as file:
            key = file.read()
        return key

    def encrypt_file(self, file_path):
        with open(file_path, "rb") as file:
            file_data = file.read()

        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(file_data)

        with open(file_path, "wb") as file:
            file.write(encrypted_data)

    def encrypt_folder(self, folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                self.encrypt_file(file_path)