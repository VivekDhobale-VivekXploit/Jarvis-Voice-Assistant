import random
import speech_recognition as sr
import webbrowser
import pyttsx3
from musicLibrary import music
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
from popularweb import websites



# -------------------------------
# Replace with your own API keys
# -------------------------------
NEWS_API_KEY = "<YOUR_NEWS_API_KEY>"
OPENAI_API_KEY = "<YOUR_OPENAI_API_KEY>"

# -------------------------------
# Initialize TTS engine (old method - unused in final)
# -------------------------------
engine = pyttsx3.init()

# -------------------------------
# Function: Speak text (gTTS + pygame)
# -------------------------------
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

# -------------------------------
# Function: Send command to OpenAI
# -------------------------------
def aiProcess(command):
    client = OpenAI(api_key=OPENAI_API_KEY)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Keep responses short."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

# -------------------------------
# Function: Process Music
# -------------------------------

def play(song_name):
    if song_name in music:
        speak(f"Playing {song_name}")
        webbrowser.open(music[song_name])
    else:
        speak("Song not found in library.")

def play_random(category="all"):
    hindi_keys = [k for k in music if not "phonk" in k and k not in ["stealth", "march", "skyfall", "wolf"]]
    phonk_keys = [k for k in music if "phonk" in k or k in ["matuska", "bana_passo", "motango_tomada"]]
    
    if category == "hindi":
        song = random.choice(hindi_keys)
    elif category == "phonk":
        song = random.choice(phonk_keys)
    else:
        song = random.choice(list(music.keys()))
    
    play(song)

# -------------------------------
# Function: Process user commands
# -------------------------------
def processCommand(c):
    c = c.lower()

    # Open website command
    if c.startswith("open "):
        site = c.replace("open ", "").strip()
        if site in websites:
            speak(f"Opening {site}")
            webbrowser.open(websites[site])
        else:
            speak(f"Sorry, I don't know the website '{site}' yet.")
        return

    # Play specific song
    elif c.startswith("play "):
        song = c.split(" ", 1)[1]
        if song.startswith("random hindi"):
            play_random("hindi")
        elif song.startswith("random phonk"):
            play_random("phonk")
        elif song.startswith("random"):
            play_random("all")
        else:
            play(song)
        return

    # Get latest news
    elif "news" in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}")
        if r.status_code == 200:
            articles = r.json().get('articles', [])
            for article in articles[:5]:
                speak(article['title'])
        else:
            speak("Unable to fetch news.")
        return

    # AI-generated response for unknown commands
    else:
        output = aiProcess(c)
        speak(output)

# -------------------------------
# Main program loop
# -------------------------------
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=3, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error:", e)

