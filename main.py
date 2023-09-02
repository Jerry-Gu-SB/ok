import keyboard
import pygame

pygame.mixer.init()

RammusOK = "Rammus OK..wav"
OOF = "3"


def play_audio():
    audio_file = RammusOK
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()


keyboard.add_hotkey('q', lambda : play_audio())
keyboard.wait()
