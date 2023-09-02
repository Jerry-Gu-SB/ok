import keyboard
import pygame

FRENCHY = False

pygame.mixer.init()
pygame.mixer.set_num_channels(100)

q_audio = "Rammus OK..wav"
w_audio = "Mhm.ogg"
e_audio = "Yep.ogg"
r_audio = "Alright.ogg"
f_audio = "what the fuck.ogg"
d_audio = "HM.ogg"
tab_audio = "Right.ogg"


def play_audio(audio_file):
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()


def FRENCH():
    global q_audio, w_audio, e_audio, r_audio, d_audio, tab_audio
    global FRENCHY
    play_audio(f_audio)
    if FRENCHY:
        FRENCHY = False
        q_audio = "Rammus OK..wav"
        w_audio = "Mhm.ogg"
        e_audio = "Yep.ogg"
        r_audio = "Alright.ogg"
        d_audio = "HM.ogg"
        tab_audio = "Right.ogg"
    else:
        FRENCHY = True
        q_audio = "OUIIIIIIII.ogg"
        w_audio = "SAAAAAAAA UUUUUURGH.ogg"
        e_audio = "OOOOOOOOHHHHHHHHHHH.ogg"
        r_audio = "HMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.ogg"
        d_audio = "WOOA PUP.ogg"
        tab_audio = "EHHHHH.ogg"


keyboard.add_hotkey('q', lambda: play_audio(q_audio))
keyboard.add_hotkey('w', lambda: play_audio(w_audio))
keyboard.add_hotkey('e', lambda: play_audio(e_audio))
keyboard.add_hotkey('r', lambda: play_audio(r_audio))

keyboard.add_hotkey('f', lambda: FRENCH())
keyboard.add_hotkey('d', lambda: play_audio(d_audio))

keyboard.add_hotkey('tab', lambda: play_audio(tab_audio))

keyboard.wait()
