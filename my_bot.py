import pyttsx3
import speech_recognition as sr
import pywhatkit
from datetime import datetime
import geocoder
import webbrowser, requests
import bs4
from bs4 import BeautifulSoup
import math
import os
import subprocess
import time
from playsound import playsound
import winsound
import selenium
import spotipy

'''To give the location'''
g = geocoder.ip('me')


listener = sr.Recognizer()
engine = pyttsx3.init()
sound = engine.getProperty('voices')
engine.setProperty("voice", sound[1].id)



url='https://www.google.com/search?q=weather'
weather=requests.get(url)
bs=bs4.BeautifulSoup(weather.text,'html.parser')
temp=bs.find('div' ,class_="BNeawe iBp4i AP7Wnd").get_text()
a=len(temp)

p_id_generated=[]

def open_is_first(command):
    if command[0:5]=='open ':
        return 1
    else:
        return 0

def close_is_first(command):
    if command[0:6]=='close ':
        return 1
    else:
        return 0

def play_is_first(command):
    if command[0:5]=='play ':
        return 1
    else:
        return 0


def play_youtube(command):
    command1 = command.replace('play','playing')
    engine.say(command1+', youtube.')
    engine.runAndWait()
    pywhatkit.playonyt(command)


def search_web(command):
    engine.say('searching web for ' + command)
    engine.runAndWait()
    pywhatkit.search(command)

def news_flash():
    v = 'https://inshorts.com/en/read'
    n = requests.get(v)
    bs = bs4.BeautifulSoup(n.text, 'html.parser')
    v = bs.find('div', class_='card-stack').find_all('span', itemprop='headline')

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)

    for i in range(0, 10):
        engine.say(v[i].get_text())
        engine.runAndWait()

#def chg_wp():

def start():

  engine.say('How may i help you today?')
  engine.runAndWait()



  with sr.Microphone() as source:



    while 1:

        print('listening....')
        engine.setProperty('rate', 200)
        while 1:

            try:

              voice = listener.listen(source, phrase_time_limit=5)
              command = listener.recognize_google(voice)
              cmd_l=command.lower()
              break
            except:
               pass
        command_l=command.lower()
        if command_l == 'code 0 0 7' or command_l == 'code 2007':
            print(command_l)
            playsound('bye_bye.mp3')
#           kill_generated_processes()
            break
        print(command)


        if play_is_first(command_l) :
            play_youtube(command_l)

        elif command_l=='change wallpaper':
            chg_wp()

        elif 'news' in command_l:
            news_flash()

        elif ('what is' in command_l and ('+' in command_l or '-' in command_l or 'x' in command_l or 'into' in command_l or 'divided by' in command_l) ):
            command_l=command_l.replace('what is', '')
            print(command_l)


            if 'x' in command_l or 'into' in command_l:
                if 'x' in command_l:
                    command_l1=command_l.replace('x','*')
                    command_l = command_l.replace('x', 'multiplied by')
                else:
                    command_l1 = command_l.replace('into', '*')


            elif 'divided by' in command_l:
                command_l1=command_l.replace('divided by','/')

            elif '-' in command_l:
                command_l1 = command_l
                command_l=command_l.replace('-','minus')

            else:
                command_l1=command_l

            a=eval(command_l1)
            print(a)

            engine.say(str(command_l) + ' is '+str(a))
            engine.runAndWait()

        elif 'who is' in command_l:
            person = command_l.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)

        elif 'joke' in command:
            talk(pyjokes.get_joke())


        elif 'roll a dice' in command:
            number = random.randint(0, 6)
            print(number)
            talk(number)


        elif open_is_first(command_l):

            if 'youtube' in command_l:
                engine.say('What would you like to watch on youtube?')
                engine.runAndWait()
                v = listener.listen(source,phrase_time_limit=5)
                vid = listener.recognize_google(v)
                engine.say('opening youtube.')
                engine.runAndWait()
                webbrowser.open('https://www.youtube.com/results?search_query='+vid.lower())


            elif 'settings' in command_l:
                os.system('start ms-settings:')

            elif 'command' in command_l:
                os.system('cmd')


            elif command_l[len(command_l)-2:len(command_l)]=='nt':

                os.system('\"C:\Riot Games\Riot Client\RiotClientServices.exe\" --launch-product=valorant --launch-patchline=live')

            elif 'facebook' in command_l:
                 engine.say('opening youtube')
                 engine.runAndWait()
                 webbrowser.open_new('https://www.facebook.com/')

            elif 'chrome' in command_l:
                engine.say('opening google chrome')
                engine.runAndWait()
                subprocess.call("C://Program Files//Google//Chrome//Application//chrome.exe ")

            elif 'telegram' in command_l:
                engine.say('opening telegram')
                engine.runAndWait()
                subprocess.call('C:/Program Files/Telegram Desktop/Telegram.exe')
                print('1')

            elif 'whatsapp' in command_l:
                engine.say('opening whatsapp')
                engine.runAndWait()
                subprocess.call('C://Users//91967//AppData//Local//WhatsApp//WhatsApp.exe')

            elif 'brave' in command_l:

                engine.say('opening brave')
                engine.runAndWait()
                subprocess.call('C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe')

            elif 'python' in command_l or 'pycharm' in command_l:
                engine.setProperty('rate', 150)
                engine.say('opening Picharm')
                engine.runAndWait()
                subprocess.call('C://Program Files//JetBrains//PyCharm Community Edition 2020.3//bin//pycharm64.exe')


        elif close_is_first(command_l):

            if 'youtube' in command_l:
                    engine.say('closing youtube.')
                    engine.runAndWait()
                    os.system('TASKKILL /F /IM brave.exe')


            elif 'chrome' in command_l:
                    engine.say('closing chrome')
                    engine.runAndWait()
                    os.system('TASKKILL /F /IM chrome.exe')

            elif 'telegram' in command_l:
                    engine.say('closing telegram')
                    engine.runAndWait()
                    os.system('TASKKILL /F /IM telegram.exe')

            elif 'whatsapp' in command_l:
                    engine.say('closing whatsapp')
                    engine.runAndWait()
                    os.system('TASKKILL /F /IM WhatsApp.exe')

            elif 'brave' in command_l:
                    engine.say('closing brave')
                    engine.runAndWait()
                    os.system('TASKKILL /F /IM brave.exe')

        else:
            search_web(command)

i=1



with sr.Microphone() as source:

           engine.say(' Hello sir, this is your friend, Joee. Your password please')
           engine.runAndWait()
           playsound('command.mp3')
           while(i==1):                   voice = listener.listen(source, phrase_time_limit=5)
                   command = listener.recognize_google(voice)
                   print(command.lower())
                   if command.lower() == 'how you doing' or command.lower() == 'how you doin' or command.lower() == 'how are you doing' or command.lower() == 'how are you doin':
                      i=i+1

                      engine.setProperty('rate', 180)
                      engine.say('Password Verified, Welcome to the world of Automation. '
                                 #'The current time, is '+datetime.now().strftime("%H Hours and %M Minutes. ")+
                                 #'Your location, is '+str(g.latlng[0])+'° North  and  '+str(g.latlng[1])+'° East. '
                                 #'Temperature, is '+temp[:a-1]+'Celcius '
                                 )
                      engine.runAndWait()








                      start()

                   else:
                      engine.say('Wrong Password. Please try again.')
                      engine.runAndWait()








