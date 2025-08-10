# Sara-Assistant
SARA (Smart AI for Reliable Assistance) is a Python-based voice assistant that uses speech recognition, OpenAI, and automation features to perform tasks like playing music, fetching news, opening websites, and sending WhatsApp messages.

 SARA — Smart AI for Reliable Assistance
SARA is a Python-based voice assistant that listens to your commands and executes them. It
includes AI responses, web search, music playback, news fetching, and WhatsApp messaging
features.
■ Features
• ■ Voice Commands Recognition (Speech-to-Text)
• ■ AI Chat (OpenAI GPT-3.5-Turbo)
• ■ Web Automation (Google, YouTube, Facebook, LinkedIn)
• ■ Song Search & Play (Fuzzy Matching from Music Library)
• ■ Latest News (NewsAPI)
• ■ Send WhatsApp Messages (PyWhatKit)
• ■ Text-to-Speech (gTTS + Pygame)
■ Folder Structure
SARA/ ■■■ sara.py # Main assistant code ■■■ musicLibrary.py # Music
links database ■■■ contact_list.py # Saved contacts ■■■ .env # API keys
(Not uploaded on GitHub) ■■■ requirements.txt # Python dependencies ■■■
README.md
■ Installation & Setup
1. Clone this repository: git clone
https://github.com/your-username/Sara-Assistant.git cd Sara-Assistant 2.
Install dependencies: pip install -r requirements.txt 3. Create `.env`
file and add your API keys: OPENAI_API_KEY=your_openai_key
NEWS_API_KEY=your_newsapi_key 4. Run the assistant: python sara.py
■ Requirements
Python 3.8+ Libraries: speechrecognition, gTTS, pygame, openai,
fuzzywuzzy, python-dotenv, pywhatkit, requests
■ Notes
• Do not upload your `.env` file to GitHub.
• For WhatsApp messaging, ensure your system time is accurate.
• For news fetching, you need a free API key from NewsAPI.
■■■ Author
Satyam LinkedIn: https://www.linkedin.com/in/satyam4561 GitHub: https://github.com/satyam-2309
