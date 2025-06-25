import streamlit as st
import json
import random
import time
import google.generativeai as genai

# Replace this with your actual Gemini API key
genai.configure(api_key="AIzaSyCQU2FN0HEBQE5J0c895-SnWCThiX_1y7A")

st.set_page_config(page_title="🚑 AmbuBuddy: AI Emergency Dispatcher", layout="centered")
st.title("🚑 AmbuBuddy – AI-Powered Emergency Help (Gemini Edition)")

st.markdown("Speak or type your emergency in Hindi or English:")

# Inject OmniDimension Widget
st.components.v1.html("""
<script id="omnidimension-web-widget"
  async
  src="https://backend.omnidim.io/web_widget.js?secret_key=742b8a46c435b040ac1eebac1126883a">
</script>
""", height=0)

# Emergency keywords
emergency_keywords = {
    "heart": "Cardiac Arrest",
    "attack": "Cardiac Arrest",
    "saans": "Breathing Problem",
    "accident": "Accident",
    "fracture": "Bone Injury",
    "blood": "Severe Bleeding",
    "bukhar": "High Fever",
    "behosh": "Unconscious"
}

def classify_emergency(text):
    for k, v in emergency_keywords.items():
        if k in text.lower():
            return v
    return "General Medical Emergency"

def find_hospital(location="Najarapur"):
    hospitals = [
        {"name": "Jeevan Raksha Hospital", "distance": "4.2 km", "eta": "10 min"},
        {"name": "Swasthya Seva Clinic", "distance": "6.8 km", "eta": "15 min"},
        {"name": "Arogya Care Centre", "distance": "9.1 km", "eta": "19 min"},
    ]
    return random.choice(hospitals)

def get_first_aid(emergency_type):
    if emergency_type == "Cardiac Arrest":
        return "- Lay the person flat\n- Loosen clothing\n- Begin CPR if trained\n- Do not give food/water"
    elif emergency_type == "Breathing Problem":
        return "- Keep person upright\n- Encourage slow, deep breathing\n- Loosen clothes"
    else:
        return "Stay calm. Help is on the way. Provide comfort and avoid moving the patient unnecessarily."

def ai_response_with_gemini(user_msg):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_msg)
        return response.text
    except Exception as e:
        return "⚠️ Gemini AI unavailable. Please try again later."

# Streamlit input
user_input = st.text_input("👤 Your Statement (e.g., 'Papa ko heart attack ho gaya')", "")

# Main logic
if user_input:
    st.info("🔍 Detecting emergency type...")
    time.sleep(1)
    emergency_type = classify_emergency(user_input)
    st.success(f"🧠 Emergency Detected: {emergency_type}")

    st.info("🚨 Searching for nearest available ambulance...")
    time.sleep(1)
    hospital = find_hospital()
    st.success(f"✅ Ambulance Dispatched from: {hospital['name']}")
    st.markdown(f"📍 Distance: {hospital['distance']} | ETA: {hospital['eta']}")

    st.markdown("---")
    st.subheader("🗣️ First Aid Instructions")
    st.markdown(get_first_aid(emergency_type))

    st.audio("assets/alert.mp3")

    st.markdown("---")
    st.subheader("🤖 Gemini AI Agent Response")
    st.markdown(ai_response_with_gemini(user_input))
else:
    st.warning("Please enter a statement to simulate an emergency.")

st.markdown("---")
st.caption("Made for Code for Bharat 🇮🇳 – Powered by Gemini AI 🚑")
