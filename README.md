# Jarvis - Voice-Controlled Personal Assistant

Jarvis is a Python-based voice assistant that responds to voice commands like opening websites, playing music, fetching news, and answering questions using Google's Gemini API. It uses speech recognition, text-to-speech, and integrates with online APIs to deliver a smart assistant experience.

---

## 🔧 Features

- 🎤 Voice Activation with "Jarvis" wake word
- 🌐 Opens popular websites like Google, YouTube, WhatsApp, etc.
- 📰 Reads top Indian news headlines using World News API
- 🎵 Plays songs using a custom music library
- 🧠 AI-powered responses via Gemini API (Google's Generative AI)

---

## 🧩 Technologies Used

- `speech_recognition` – for recognizing voice commands
- `pyttsx3` – for text-to-speech output
- `requests` – for API communication
- `webbrowser` – to open URLs
- `musiclibrary` – custom module for song mapping
- Gemini API – AI responses
- World News API – latest headlines

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/jarvis-assistant.git
   cd jarvis-assistant


##UPDATE IN main FILE

GEMINI_API_KEY = "your_gemini_api_key"
NEWS_API_KEY = "your_world_news_api_key"
