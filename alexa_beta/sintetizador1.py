import pyttsx3

robo = pyttsx3.init()
robo.setProperty('volume', 1.0)
robo.setProperty('rate', 130)
robo.setProperty('voice', r'')
msg = "so quer mamão so quer mel"
robo.say(msg)
robo.runAndWait()

for sintetizador in robo.getProperty('voices'):
    print(sintetizador)
