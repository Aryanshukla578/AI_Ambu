# 🚑 AI_Ambu – Intelligent Emergency Dispatcher for Bharat

**AI_Ambu** is an AI-powered emergency assistant that helps citizens in **rural and urban India** request ambulances using voice or text. It auto-classifies emergencies, provides first aid, and dispatches help from the nearest hospital. Designed for fast response, low-tech regions, and language inclusivity (especially Hindi and tier-2/3 areas).

🔗 **Website Agent Link:** [https://v0-ai-ambu-website-creation.vercel.app/](https://v0-ai-ambu-website-creation.vercel.app/)
🔗 **Agent app link:** [https://envious-degree-7953.glide.page](https://envious-degree-7953.glide.page)
---

## 🧠 Key Features

- 🔊 Accepts **Hindi/English** voice or typed emergency descriptions  
- 🧠 Classifies emergency types like: **Cardiac Arrest, Accident, Breathing Issues**  
- 📍 Finds **nearest hospital or ambulance** (static or map-based simulation)  
- 🗣️ Gives **real-time first aid instructions**  
- 📲 Sends alert messages to **emergency contacts** (simulated)  
- 🖥️ Built with a **Streamlit-based GUI** for easy demo and testing  

---

## 🛠️ Tech Stack

| Layer            | Tech Used                    |
|------------------|------------------------------|
| Frontend GUI     | `Streamlit`                  |
| Backend Logic    | `Python`, `Regex/NLP`        |
| Emergency Logic  | `Custom Keyword Classifier`  |
| Text-to-Speech   | `gTTS`, `pyttsx3` *(optional)* |
| Audio Alerts     | `playsound`, `Streamlit Audio` |

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/Aryanshukla578/AI_Ambu.git
cd AI_Ambu
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 🧪 Sample Use Cases

| User Statement                    | Detected Emergency     |
|----------------------------------|-------------------------|
| "Mummy ko saans nahi aa rahi"   | Breathing Problem       |
| "Papa behosh ho gaye hain"      | Unconsciousness         |
| "Accident ho gaya"              | Road Accident           |
| "Dil me dard ho raha hai"       | Cardiac Arrest          |
| "Kisi ko chot lag gayi hai"     | Injury / Trauma         |

---

## 📁 Folder Structure

```
AI_Ambu/
├── app.py                  # Main Streamlit app
├── assets/
│   └── alert.mp3           # Emergency sound alert
├── logic/
│   └── classify.py         # Emergency detection logic
├── requirements.txt
└── README.md
```

---

## 🎯 Vision

**AI_Ambu** aims to bridge the **critical gap** between emergency victims and response teams, particularly in **underserved regions** of Bharat.  
It’s built to be fast, lightweight, and functional **even in low-resource settings** using AI, NLP, and community-first principles.

---

## 👤 Created by Aryan Shukla  
**Part of Code for Bharat initiatives**  
🌐 GitHub: [github.com/Aryanshukla578](https://github.com/Aryanshukla578)
