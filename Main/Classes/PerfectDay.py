import pygame



class MusicPlayer:
    def __init__(self, music_file):
        self.music_file = music_file

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play(-1)  # -1 geeft aan dat het nummer herhaaldelijk moet worden afgespeeld

    def stop_music(self):
        pygame.mixer.music.stop()
        print("Het afspelen is gestopt.")


# Voorbeeldgebruik:
#music_file = "Perfect Day_50.mp3"
#player = MusicPlayer(music_file)
#player.play_music()

# Stop het afspelen als de gebruiker "666" invoert
#user_input = ""
#while user_input != "666":
# Rolling Stones - Sympathy for the Devil
    #user_input = input("Tell me what's my name: ")

#player.stop_music()
