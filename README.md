# Jarvis-Voice-Assistant
A simple Python-based voice assistant that responds to the wake word “Jarvis”, opens websites, plays music, fetches news, and answers questions using OpenAI GPT-3.5.
# Jarvis Voice Assistant 🎙️

A simple Python voice assistant that can:
- Open popular websites
- Play songs from a preset library
- Fetch latest news headlines
- Answer questions using OpenAI GPT-3.5

## 📌 Features
- **Wake Word**: Say `"Jarvis"` to activate.
- **Web Shortcuts**: Open Google, Facebook, YouTube, LinkedIn.
- **Music Player**: Play songs from `musicLibrary.py`.
- **News**: Get latest top headlines from India.
- **AI Chat**: Ask Jarvis anything, powered by GPT-3.5.

## 🛠 Requirements
Install dependencies:
```bash
pip install -r requirements.txt
```

## 🔑 API Keys
You need:
- **OpenAI API Key** → [Get here](https://platform.openai.com/)
- **NewsAPI Key** → [Get here](https://newsapi.org/)

Replace in:
- `main.py` → `OPENAI_API_KEY` and `NEWS_API_KEY`
- `client.py` → `OPENAI_API_KEY`

## 🚀 Run the Assistant
```bash
python main.py
```

Then:
1. Wait for `"Listening for wake word..."`.
2. Say `"Jarvis"`.
3. Give a command like:
   - `"Open Google"`
   - `"Play stealth"`
   - `"News"`
   - `"Who is Elon Musk?"`

## 📂 File Structure
```
Jarvis/
│── main.py          # Main assistant program
│── client.py        # Simple GPT-3.5 test script
│── musicLibrary.py  # Song library
│── requirements.txt # Dependencies
│── README.md        # Documentation
```

## 📝 Notes
- Requires **microphone access** for speech recognition.
- Uses Google Speech Recognition (requires internet).
- For music, add your own songs to `musicLibrary.py`.

