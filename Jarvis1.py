import speech_recognition as sr  # Importation du module de reconnaissance vocale
import pyttsx3                  # Importation du module de synthèse vocale
import pywhatkit                # Importation du module pour jouer de la musique sur YouTube
import datetime                 # Importation du module pour gérer les dates et les heures

# Initialisation du moteur de reconnaissance vocale et de synthèse vocale
listener = sr.Recognizer()
engine = pyttsx3.init()

# Configuration des propriétés pour le moteur de synthèse vocale
# En supposant que 'french' est un ID de voix valide, cela définit la voix en français
engine.setProperty('voice', 'french')  

def speak(text):
    """Fonction qui permet au programme de prononcer le texte donné."""
    engine.say(text)
    engine.runAndWait()  # Bloque tant que tout le texte n'est pas lu

def listen():
    """Fonction qui écoute la commande vocale de l'utilisateur et renvoie le texte reconnu."""
    command = ''
    with sr.Microphone() as source:  # Utilise le microphone par défaut comme source audio
        try:
            print("je suis à l'écoute...")  # Affichage dans la console pour indiquer que l'IA écoute
            voice = listener.listen(source, timeout=5, phrase_time_limit=7)  # Ecouter pendant 5 secondes max
            # Conversion de la parole en texte
            command = listener.recognize_google(voice, language='fr-FR')
        except sr.UnknownValueError:  # Gestion du cas où le discours n'est pas compris
            speak('Je suis désolé, je n\'ai pas compris.')
        except sr.RequestError:  # Erreur si le service de reconnaissance vocale n'est pas accessible
            speak('Erreur de service; vérifiez votre connexion Internet.')
        except Exception as e:  # Capture des autres exceptions générales
            print(f"Une erreur est survenue : {e}")
    return command.lower()  # Retourne la commande en minuscules pour faciliter la correspondance avec les mots clés

def run_assistant():
    """Fonction principale exécutant l'assistant pour traiter les commandes utilisateur."""
    command = listen()  # Récupère la commande de l'utilisateur
    if command:
        print(command)  # Affiche la commande pour débogage
        if 'bonjour' in command:
            speak('Bonjour, comment ça va?')
        elif 'oui' in command:
            speak('Oui, ça va de mon côté. Comment puis-je aider?')
        elif 'mettez la musique de votre choix de' in command:
            artist = command.replace('mettez la musique de votre choix de ', '')  # Extrait le nom de l'artiste
            pywhatkit.playonyt(artist)  # Joue une vidéo de l'artiste sur YouTube
        elif 'heure' in command:
            # Obtention de l'heure actuelle et formatage en heures et minutes
            time = datetime.datetime.now().strftime('%H:%M')
            speak(f'Il est {time}')  # Annonce l'heure
        elif 'ton nom' in command:
            speak("Je m'appelle NANA.")  # Réponse de l'assistant à la question de son nom

if __name__ == '__main__':
    while True:  # Boucle infinie pour que l'assistant reste actif
        run_assistant()  # Lancement de la fonction principale 



"""
Le code fourni est un script Python qui sert de base pour un assistant vocal en langue française. Voici une explication du code, segment par segment.

### Importations des modules
```python
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
```
Des modules sont importés en préparation pour les différentes fonctionnalités de l'assistant:
- `speech_recognition` pour la reconnaissance vocale;
- `pyttsx3` pour la synthèse vocale;
- `pywhatkit` pour jouer de la musique sur YouTube;
- `datetime` pour obtenir et traiter les dates et heures.

### Initialisation et configuration du moteur de reconnaissance et de synthèse vocale
```python
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice', 'french')
```
Un objet `Recognizer` est créé pour reconnaître la parole. Le moteur de synthèse vocale est initialisé avec `pyttsx3` et configuré pour utiliser une voix en français.

### Fonctions `speak` et `listen`
```python
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    ...
```
Deux fonctions sont définies pour interpréter le texte (`speak`) et écouter puis renvoyer la commande vocale de l'utilisateur (`listen`). `listen` utilise l'objet `Recognizer` pour écouter via le microphone et reconnaît le langage avec Google Speech Recognition API, gérant certaines exceptions courantes.

### Fonction `run_assistant`
```python
def run_assistant():
    ...
```
Cette fonction principale attend les commandes de l’utilisateur, reçues et traitées par la fonction `listen`. Selon la commande reçue, l'assistant réagit différemment :
- Salutations si on dit "bonjour";
- Réponse affirmative si on dit "oui";
- Jouer de la musique d'un artiste spécifique demandé;
- Dire l'heure actuelle si on demande l'heure;
- Se présenter si on lui demande son nom.

### Boucle principale
```python
if __name__ == '__main__':
    while True:
        run_assistant()
```
Cette portion assure que le code exécute la fonction `run_assistant` dans une boucle infinie seulement si le script est exécuté comme programme principal (pas importé comme un module). Cela permet à l’assistant de continuer à répondre aux commandes indéfiniment.

En conclusion, ce code complet crée un assistant vocal simple capable de comprendre et répondre en français à certaines commandes basiques vocales de l'utilisateur. Il utilise la reconnaissance vocale pour détecter les commandes et interagit via la synthèse vocale, et est capable d'effectuer des actions telles que jouer de la musique ou fournir l'heure actuelle.
"""



