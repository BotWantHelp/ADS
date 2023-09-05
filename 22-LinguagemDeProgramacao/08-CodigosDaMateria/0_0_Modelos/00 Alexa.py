# pip install SpeechRecognition pyttsx3 pywhatkit pyautogui pyaudio
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import pyautogui as pa
import time
import pywhatkit as kit
import openpyxl
import datetime
import pyautogui
import time
import locale


audio = sr.Recognizer()
maquina = pyttsx3.init()

print()
def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'computador' in comando:
                comando = comando.replace('computador', '')
                maquina.say(comando)
                maquina.runAndWait()

    except sr.UnknownValueError:
        print('Não foi possível reconhecer o que foi dito.')
    except sr.RequestError as e:
        print('Não foi possível obter resposta do serviço de reconhecimento de voz; {0}'.format(e))
    except Exception as ex:
        print('Erro inesperado:', ex)

    return comando

def comando_voz_usuario(comando):
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
        print(f' Agora é: {hora}')

    elif 'toca' in comando:
        musica = comando.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando música')
        maquina.runAndWait()
    
    elif 'papagaio' in comando:
        pa.press("winleft")
        time.sleep(1)
        pa.write("cmd")
        time.sleep(1)
        pa.press("enter")
        time.sleep(1)
        pa.write("curl parrot.live")
        pa.press("enter")
        maquina.say('Abrindo Papagaio no terminal')
        maquina.runAndWait()
        
comando = executa_comando()
comando_voz_usuario(comando)

