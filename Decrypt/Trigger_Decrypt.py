from Decrypt import decrypt_folder

def main():
    folder_path = "Project_def/Main/Classes/te_versleutelen_folder"
    key_file_path = "Project_def/Main/Classes/Key.txt"

    decrypt_folder(folder_path, key_file_path)

    print("Folder is succesvol gedecrypteerd.")

if __name__ == "__main__":
    main()

