from pygame import mixer

class SoundManager:
    def __init__(self):
        # PlayList des musiques jouables en jeux
        self.playList = {
            "Transition": "Sound/Transition_Sound.wav",
            "Pc": "Sound/Pc_Sound.wav",
            "TaskDone": "Sound/TaskDone_Sound.wav",
            "Bed": "Sound/Bed_Sound.wav",
            "Social": "Sound/Social_Env_Sound.mp3",
            "Error": "Sound/Error_Sound.wav"
        }
        # Initialisation du gestionnaire de musique
        mixer.init()

    def playMusic(self, music_key) -> None:
        # Charge et joue la musique correspondant à la clé fournie
        music_file = self.playList.get(music_key)
        if music_file:
            mixer.music.load(music_file)
            mixer.music.play()