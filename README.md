# 🎙️ Whisper Voice Transcriber

This Python project lets you **record live audio from your microphone** and **transcribe it to text** using [OpenAI Whisper](https://github.com/openai/whisper).  
It records up to 15 seconds of speech (or less if you stop early with `Ctrl + C`), then transcribes it automatically.

---

## 🚀 Features
- 🎤 Live microphone recording  
- 🧠 Automatic speech-to-text using Whisper  
- 🌐 Language auto-detection or manual language selection  
- 💾 Temporary WAV file recording (auto-deleted after use)

---

## 🧩 Requirements

Make sure you have **Python 3.8+** installed.

### Install dependencies
```bash
pip install numpy sounddevice soundfile openai-whisper
