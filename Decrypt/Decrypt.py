import os
from cryptography.fernet import Fernet

def load_key_from_file(file_path):
    with open(file_path, "rb") as file:
        key = file.read()
    return key

def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def decrypt_folder(folder_path, key_file_path):
    key = load_key_from_file(key_file_path)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

