# 🚑 AI_Ambu – Intelligent Emergency Dispatcher for Bharat

**AI_Ambu** is an AI-powered emergency assistant that helps citizens in rural and urban areas request ambulances using voice or text, auto-classifies the emergency, and dispatches help from the nearest hospital. Designed for fast response and language inclusivity, especially for Hindi and tier-2/3 regions.

---

## 🧠 Key Features

- 🔊 Accepts Hindi/English voice or typed emergency descriptions
- 🧠 Classifies emergency type: Cardiac, Accident, Breathing issue, etc.
- 📍 Finds nearest ambulance/hospital (static or map-based simulation)
- 🗣️ Gives **real-time first aid instructions**
- 📲 Sends alerts to emergency contacts (simulated)
- 🎛️ Streamlit-based GUI for demo/testing

---

## 🛠️ Tech Stack

| Layer          | Tech Used                    |
|----------------|------------------------------|
| Frontend GUI   | Streamlit                    |
| Backend Logic  | Python                       |
| Emergency Logic| NLP Keyword Classifier       |
| Text-to-Speech | `gTTS`, `pyttsx3` (optional) |
| Audio Alerts   | `playsound`, `Streamlit`     |

---

## 📦 Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/Aryanshukla578/AI_Ambu.git
cd AI_Ambu
pip install -r requirements.txt
streamlit run app.py
🧪 Sample Use Cases
| Statement                     | Detected Emergency |
| ----------------------------- | ------------------ |
| "Mummy ko saans nahi aa rahi" | Breathing Problem  |
| "Papa behosh ho gaye hain"    | Unconscious        |
| "Accident ho gaya"            | Road Accident      |
| "Dil me dard ho raha hai"     | Cardiac Arrest     |

📁 Folder Structure
AI_Ambu/
├── app.py                  # Main Streamlit app
├── assets/
│   └── alert.mp3           # Audio file
├── logic/
│   └── classify.py         # Emergency classifier
├── requirements.txt
🎯 Vision
AI_Ambu aims to bridge the critical gap between emergency victims and response teams, especially in underserved regions. Built with simplicity, speed, and Bharat's diversity in mind.
🧠 Created by Aryan Shukla
Part of Code for Bharat initiatives.
GitHub • LinkedIn
