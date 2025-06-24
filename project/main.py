import requests
import json
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

# API Keys
GEMINI_API_KEY = "YOUR_API_KEY"
NEWS_API_KEY = "YOUR_API_KEY"

# Initialize recognizer and text-to-speech engine
recogniser = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text aloud
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to call Google's Gemini API for AI responses
def ask_gemini(question):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{"text": question}]
        }]
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            response_data = response.json()
            ai_response = response_data["candidates"][0]["content"]["parts"][0]["text"]
            print(f"Gemini: {ai_response}")
            speak(ai_response)
        else:
            print(f"Error {response.status_code}: {response.text}")
            speak("I couldn't get a response from the AI.")
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        speak("There was an error while communicating with the AI.")

# Function to fetch news headlines
def fetch_headlines():
    url = f'https://api.worldnewsapi.com/search-news?source-country=in&api-key={NEWS_API_KEY}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            news_items = data.get('news', [])
            for article in news_items[:5]:  # Read top 5 headlines
                print(article.get('title'))
                speak(article.get('title'))
        else:
            print(f"Error: {response.status_code} - {response.text}")
            speak("Sorry, I couldn't fetch the news.")
    except Exception as e:
        print(f"Error fetching news: {e}")
        speak("There was an error fetching the news.")

# Function to process voice commands
def processcommand(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        speak("Opening WhatsApp.")
    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn.")
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook.")
    elif command.startswith("play"):
        song = command.lower().split(" ")[1]
        link = musiclibrary.music.get(song)

        if link:
            webbrowser.open(link)
            speak(f"Playing {song}.")
        else:
            speak(f"Sorry, I couldn't find {song}.")
    elif "news" in command:
        fetch_headlines()
    elif "explain" in command or "what is" in command or "how" in command or "open" in command:
        ask_gemini(command)  # Call Gemini for AI-related questions
    else:
        speak("I didn't understand that command.")

# Main program loop
if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        print("Listening for 'Jarvis'...")

        try:
            # Listen for the wake word "Jarvis"
            with sr.Microphone() as source:
                recogniser.adjust_for_ambient_noise(source)  # Adapt to background noise
                audio = recogniser.listen(source, timeout=5, phrase_time_limit=3)

            # Recognize speech
            word = recogniser.recognize_google(audio)
            print(f"{word}")

            # Activate on "Jarvis"
            if word.lower() == "jarvis":
                speak("Yes, how can I help?")

                with sr.Microphone() as source:
                    print("Listening for command...")
                    recogniser.adjust_for_ambient_noise(source)
                    audio = recogniser.listen(source, timeout=8, phrase_time_limit=6)

                    command = recogniser.recognize_google(audio)
                    print(f"Command: {command}")
                    processcommand(command)

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except sr.RequestError:
            print("Network error. Please check your connection.")
        except Exception as e:
            print(f"Error: {e}")
