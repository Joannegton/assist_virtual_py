import datetime
from datetime import datetime
import os
import keyboard
import subprocess
import random
import requests
import pyjokes
import speech_recognition
import gtts
from gtts import gTTS
import playsound
import pywhatkit as kit
import pyttsx3
import openai
import whisper



#reconhecimento de voz e fala
def ouvir():
    sr = speech_recognition
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.8)
        print('>>>>> ouvindo...')
        r.pause_threshold = 1.2
        audio = r.listen(source)

    try:
        print('>>>> reconhecendo...')
        intent = r.recognize_google(audio, language='pt-br')
        print(f'o que eu ouvi: {intent}\n')

    except Exception as e:
        print(e)
        fale('Desculpe, não entendi. Pode repetir?.')
        return None

    return intent.lower()

def fale(text):
    #definindo a voz
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'voices[1].id')
    engine.say(text)
    engine.runAndWait()

def tecla_espaco():
    while True:
        try:
            if keyboard.is_pressed('space'):
                break
        except:
            break

def saldar():
    hora = datetime.now().hour
    if hora >= 6 and (hora <= 11):
        fale('Bom dia mestre Bolacha')
        previsao_tempo()
    elif hora >= 12 and (hora <= 18):
        fale('Boa tarde mestre Bolacha')
    else:
        fale('Boa nnoite mestre Bolacha')

def previsao_tempo():
    apiKey = 'APIKey'
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=guarulhos&appid={apiKey}&units=metric')
    x = response.json()
    if x["cod"] != "404":
        temperature = x['main']['temp']
        temp = (f'A temperatura é de {temperature} graus')
        fale(temp)
    else:
        print('desculpe, cidade não encontrada')

def abrir_camera():
    os.system('start microsoft.windows.camera:')

def escrever_txt():
    fale('o que devo escrever?')
    note_text = ouvir()
    if (note_text != None):
        f = open('textos/notes.txt', 'a')
        note = note_text + '\n\n'
        f.write(note)
        f.close()

def desligar_pc():
    desligar = fale('fale sim, para desligar, ou não, para cancelar')
    if desligar == 'não':
        exit()
    else:
        fale("até brave, senhor Stark")
        os.system('shutdown /s /t 0')

##########################################################################

def meu_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    print(type(ip_address['ip']))

def youtube(video):
    kit.playonyt(video)

def pesquisar_google(query):
    kit.search(query)

def chatgpt():
    # Transcreve o audio gravado anteriormente.
    fale('O que deseja que eu pesquise?')
    pesquisa = ouvir()
    # Configura a chave de API da OpenAI usando a variável de ambiente 'OPENAI_API_KEY'
    os.environ['OPENAI_API_KEY'] = 'apikey'
    openai.api_key = os.environ.get('OPENAI_API_KEY')

    # Envia uma requisição à API do ChatCompletion usando o modelo GPT-3.5 Turbo
    # Lembrando que, a variável 'transcription' contém a transcrição do áudio.
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[ { "role": "user", "content": pesquisa } ]
    )
    # Obtém a resposta gerada pelo ChatGPT
    chatgpt_response = response.choices[0].message.content
    string = str(chatgpt_response)
    print(string)
    fale(string)
    


