import pygame
from pygame import mixer

class SoundManager:
    def __init__(self):
        # PlayList des musiques jouables en jeux
        # Raison de performance on ne parcours pas de dossier (paramétrage arbitraire)
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
            "Error": "Sound/Error_Sound.wav",
            "Background": "Sound/Background_Sound.wav"
        }
        # Création de différent channel(piste) de son (8 channel différent par défaut)
        self.channelBackground = mixer.Channel(0) # musique de fond du jeu
        # Initialisation du gestionnaire de musique
        mixer.init()

    def fadeOutMusic(self, channel, amount) -> None:
       mixer.Channel(channel).fadeout(amount)

    def playMusic(self, music_key: str, channel: int, numberOfLoop: int, volume, fadeInMs) -> None:
        # Create an audio track with a channel number and set its volume
        channelUse = mixer.Channel(channel)
        channelUse.set_volume(volume)

        # Load and play the music corresponding to the provided key
        music_file = self.playList.get(music_key)
        sound = None  # Initialize sound variable outside the if block

        if music_file:
            # Load a sound file to play on a channel
            sound = mixer.Sound(music_file)

            # 0 loops mean played once and repeated 0 times
            channelUse.play(sound, numberOfLoop, fade_ms=fadeInMs)

    def unlaodMusic(self) -> None:
        # libère les ressources pour le fichier audio
        mixer.music.unload()