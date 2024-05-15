import speech_recognition as sr
reconhecedor = sr.Recognizer()
with sr.Microphone() as mic:
    print("Fala veinho")
    audio = reconhecedor.listen(mic, timeout=5)
    print("fale agora...")
    try:
        texto = reconhecedor.recognize_google(audio, language='pt-br')
        print(texto)
    except:
        print("não entendi")
