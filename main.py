import keyboard
import pygame

FRENCHY = False

pygame.mixer.init()
pygame.mixer.set_num_channels(100)

q_audio = r"ok\audio_files\Rammus OK..wav"
w_audio = r"ok\audio_files\Mhm.ogg"
e_audio = r"ok\audio_files\Yep.ogg"
r_audio = r"ok\audio_files\Alright.ogg"
f_audio = r"ok\audio_files\what the fuck.ogg"
d_audio = r"ok\audio_files\HM.ogg"
tab_audio = r"ok\audio_files\Right.ogg"


def play_audio(audio_file):
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()


def FRENCH():
    global q_audio, w_audio, e_audio, r_audio, d_audio, tab_audio
    global FRENCHY
    play_audio(f_audio)
    if FRENCHY:
        FRENCHY = False
        q_audio = r"ok\audio_files\Rammus OK..wav"
        w_audio = r"ok\audio_files\Mhm.ogg"
        e_audio = r"ok\audio_files\Yep.ogg"
        r_audio = r"ok\audio_files\Alright.ogg"
        d_audio = r"ok\audio_files\HM.ogg"
        tab_audio = r"ok\audio_files\Right.ogg"
    else:
        FRENCHY = True
        q_audio = r"ok\audio_files\OUIIIIIIII.ogg"
        w_audio = r"ok\audio_files\SAAAAAAAA UUUUUURGH.ogg"
        e_audio = r"ok\audio_files\OOOOOOOOHHHHHHHHHHH.ogg"
        r_audio = r"ok\audio_files\HMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.ogg"
        d_audio = r"ok\audio_files\WOOA PUP.ogg"
        tab_audio = r"ok\audio_files\EHHHHH.ogg"


keyboard.add_hotkey('q', lambda: play_audio(q_audio))
keyboard.add_hotkey('w', lambda: play_audio(w_audio))
keyboard.add_hotkey('e', lambda: play_audio(e_audio))
keyboard.add_hotkey('r', lambda: play_audio(r_audio))

keyboard.add_hotkey('f', lambda: FRENCH())
keyboard.add_hotkey('d', lambda: play_audio(d_audio))

keyboard.add_hotkey('tab', lambda: play_audio(tab_audio))

keyboard.wait()
