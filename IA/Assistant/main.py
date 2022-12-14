import speech_recognition as sr  # pour l'écoute
import pyttsx3 as ttx
import pywhatkit
import datetime

# Pour faire  parler l'assistant


def parler(text):
    engine.say(text)
    engine.runAndWait()

# En écoute de la commande utilisateur.


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


# On lance réellement l'asistant à ce niveau
# C'est a ce niveau aussi que l'on définit les actions possibles
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


###############################################
# Init au lancement
# C'est ce qui écoute
listener = sr.Recognizer()

engine = ttx.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', 'french')
###############################################

# Boucle pour se mettre en attente d'instruction
while True:
    lancer_assistant()
