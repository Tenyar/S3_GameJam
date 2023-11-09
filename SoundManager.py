import pygame
from pygame import mixer

class SoundManager:
    def __init__(self):
        # PlayList des musiques jouables en jeux
        self.playList = {
            "Transition": "Sound/Transition_Sound.wav",
            "Pc": "Sound/Pc_Sound.wav",
            "TaskDone": "Sound/TaskDone_Sound.wav",
            "TaskSuccess": "Sound/Task_Success.mp3",
            "InBed": "Sound/Jump_Bed.mp3",
            "OutBed": "Sound/Out_Bed.wav",
            "Social": "Sound/Social_Env_Sound.mp3",
            "ProgBarFull": "Sound/BarProg_Full.mp3",
            "GameOver": "Sound/GameOver",
            "Error": "Sound/Error_Sound.wav"
        }
        # Initialisation du gestionnaire de musique
        mixer.init()

    def setVolume(self, amount) -> None:
        mixer.music.set_volume(amount)

    def playMusic(self, music_key) -> None:
        # Charge et joue la musique correspondant à la clé fournie
        music_file = self.playList.get(music_key)
        if music_file:
            mixer.music.load(music_file)
            mixer.music.play()

    def unlaodMusic(self) -> None:
        # libère les ressources pour le fichier audio
        mixer.music.unload()