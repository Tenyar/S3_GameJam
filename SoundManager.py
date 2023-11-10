import pygame
from pygame import mixer

class SoundManager:
    def __init__(self):
        # PlayList des musiques jouables en jeux
        # Raison de performance on ne parcours pas de dossier (paramétrage arbitraire)
        transitionSound = mixer.Sound("Sound/Transition_Sound.wav")
        pcSound = mixer.Sound("Sound/Pc_Sound.wav")
        taskDoneSound = mixer.Sound("Sound/TaskDone_Sound.wav")
        taskSucessSound = mixer.Sound("Sound/Task_Success.mp3")
        inBedSound = mixer.Sound("Sound/Jump_Bed.mp3")
        outBedSound = mixer.Sound("Sound/Out_Bed.wav")
        socialSound = mixer.Sound("Sound/Social_Env_Sound.mp3")
        progBarFullSound = mixer.Sound("Sound/BarProg_Full.mp3")
        #gameOverSound = mixer.Sound("Sound/GameOver")
        errorSound = mixer.Sound("Sound/Error_Sound.wav")
        backgroundSound = mixer.Sound("Sound/Background_Sound.wav")

        self.playList = {
            "Transition": transitionSound,
            "Pc": pcSound,
            "TaskDone": taskDoneSound,
            "TaskSuccess": taskSucessSound,
            "InBed": inBedSound,
            "OutBed": outBedSound,
            "Social": socialSound,
            "ProgBarFull": progBarFullSound,
            #"GameOver": gameOverSound,
            "Error": errorSound,
            "Background": backgroundSound
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
        sound = None  # Initialize sound variable outside the if block
        sound = self.playList.get(music_key)

        if sound:
            # Load a sound file to play on a channel
            #sound = mixer.Sound(sound)

            # 0 loops mean played once and repeated 0 times
            channelUse.play(sound, numberOfLoop, fade_ms=fadeInMs)

    def unlaodMusic(self) -> None:
        # libère les ressources pour le fichier audio
        mixer.music.unload()