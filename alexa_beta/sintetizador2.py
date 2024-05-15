from gtts import gTTS
from pygame import mixer, time

voz = gTTS("Olá mundo", lang='pt-br')
voz.save("olamundo.mp3")
mixer.init()
mixer.music.load("olamundo.mp3")
mixer.music.play()
input()
