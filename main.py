import speech_recognition as sr
import webbrowser
import musicLibrary
import requests
from gtts import gTTS
import pygame
import os
import openai
from fuzzywuzzy import process
from dotenv import load_dotenv
import pywhatkit
import datetime
import contact_list  # your contact file

# Load API Keys
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
newsapi = os.getenv("NEWS_API_KEY")

recognizer = sr.Recognizer()

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    pygame.quit()
    os.remove("temp.mp3")

def aiProcess(command):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are SARA, a helpful AI assistant."},
            {"role": "user", "content": command}
        ]
    )
    return response['choices'][0]['message']['content']

def sendWhatsappMessage(name, msg):
    number = contact_list.contacts.get(name.lower())
    if number:
        now = datetime.datetime.now() + datetime.timedelta(minutes=1)
        hour, minute = now.hour, now.minute
        pywhatkit.sendwhatmsg(number, msg, hour, minute)
        speak(f"Sending message to {name}")
    else:
        speak(f"Contact {name} not found.")

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif "play" in c:
        if c.startswith("play song"):
            song_input = c.replace("play song", "").strip()
        else:
            song_input = c.replace("play", "").strip()

        all_songs = list(musicLibrary.music.keys())
        best_match, score = process.extractOne(song_input, all_songs)

        if score > 70:
            link = musicLibrary.music[best_match]
            speak(f"Playing {best_match}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find a match for {song_input}")

    elif "news" in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles[:5]:
                speak(article['title'])
        else:
            speak("Sorry, I couldn't fetch the news right now.")

    elif "send message to" in c:
        try:
            name = c.split("send message to")[1].split("saying")[0].strip()
            msg = c.split("saying")[1].strip()
            sendWhatsappMessage(name, msg)
        except:
            speak("Sorry, I couldn't understand the message format.")

    else:
        output = aiProcess(c)
        speak(output)

# ------------ MAIN PROGRAM LOOP ------------
if __name__ == "__main__":
    speak("Initializing SARA...")
    speak("Hello, I am SARA. Your personal AI assistant is now online.")
    
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)
                print("You said:", word)

                if word.lower() == "sara":
                    speak("Yes?")
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        print("Command:", command)
                        processCommand(command)

        except Exception as e:
            print("Error:", e)
