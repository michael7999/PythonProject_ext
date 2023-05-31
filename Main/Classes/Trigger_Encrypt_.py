import os

from Encrypt_ import FileEncryptor

class FolderEncryptor:
    def __init__(self, folder_path, key_file_path):
        self.folder_path = folder_path
        self.key_file_path = key_file_path

    def encrypt_folder(self):
        encryptor = FileEncryptor(self.key_file_path)

        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                encryptor.encrypt_file(file_path)