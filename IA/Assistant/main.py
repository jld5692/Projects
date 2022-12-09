import speech_recognition as sr  # pour l'écoute
import pyttsx3 as ttx
import pywhatkit
import datetime


def parler(text):
    engine.say(text)
    engine.runAndWait()


def ecouter():
    try:
        with sr.Microphone() as source:
            print("Parler maintenant")
            voix = listener.listen(source)
            command = listener.recognize_google(
                voix, language='fr-FR', show_all=False)
            command.lower()
    except:
        pass
    return command


def lancer_assistant():
    command = ecouter()
    print(command)
    if 'Bonjour' in command:
        text = 'bonjour, ca va ?'
        parler(text)
    elif 'mets la chanson de' in command:
        # on vide le début de la commande pour ne garder que le nom de l'artiste
        chanteur = command.replace('mets la chanson de', '')
        print(chanteur)
        pywhatkit.playonyt(chanteur)
    elif 'heure' in command:
        heure = datetime.datetime.now().strftime('%H:%M')
        parler("il est"+heure)
    else:
        parler('Je ne comprends pas')


# C'est ce qui écoute
listener = sr.Recognizer()

engine = ttx.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', 'french')

while True:
    lancer_assistant()
