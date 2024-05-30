import speech_recognition  as sr # type: ignore
import pyttsx3 # type: ignore
import pywhatkit # type: ignore
import urllib.request
import json

name = 'alexa'
key = 'AIzaSyACh5s998R_YhEqffTiF-xwFlprKM0lx0s'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:    
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
    except:
        pass
    return rec

def run():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('reproduciendo' + music)
        pywhatkit.playonyt(music)

    if 'cuantos suscriptores tiene' in rec:
        name_subs = rec.replace('cuantos suscriptores tiene', '')
        data = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=' + name_subs.strip() + '&key=' + key).read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        talk(name_subs + " tiene{:,d}".format(int(subs)) + " suscriptores!")
        
run()