import speech_recognition as sr
import os

def ouve_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        #Algoritmo reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        print("Diga alguma coisa:")

        audio = microfone.listen(source)
    
    try:

        #Cadastro de variáveis para reconhecimento de padrões
        frase = microfone.recognize_google(audio,language='pt-BR')

        if "navegador" in frase:
            os.system("start Chrome.exe")
            return False
        
        elif: "Excel" in frase:
            os.system("start Excel.exe")
            return False
        
        elif "PowerPoint" in frase:
            os.system("start POWERPNT.exe")
            return False
        
        elif "Edge" in frase:
            os.system("start msedge.exe")
            return False
        elif "Fechar" in frase:
            os.system("exit")
            return True
        
        print("Você disse:" + frase)

    # Caso não reconheça a fala ou padrão de fala
    except sr.UnkownValueError:
        print("Não compreendi")

    return frase

while True:
    if ouve_microfone():
        break

        
