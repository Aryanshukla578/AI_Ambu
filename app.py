import streamlit as st
import json
import random
import time
import openai

# Replace with your OpenAI key
openai.api_key = "sk-your-key"

# Streamlit setup
st.set_page_config(page_title="🚑 AmbuBuddy: AI Emergency Dispatcher", layout="centered")
st.title("🚑 AmbuBuddy – AI-Powered Emergency Help (Bharat Focused)")

st.markdown("Speak or type your emergency in Hindi or English:")

# OmniDimension Chat Widget
st.components.v1.html("""
<script id="omnidimension-web-widget"
  async
  src="https://backend.omnidim.io/web_widget.js?secret_key=742b8a46c435b040ac1eebac1126883a">
</script>
""", height=0)

# User input
user_input = st.text_input("👤 Your Statement (e.g., 'Papa ko heart attack ho gaya')", "")

# Emergency type classifier
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

# Hospital locator simulation
def find_hospital(location="Najarapur"):
    hospitals = [
        {"name": "Jeevan Raksha Hospital", "distance": "4.2 km", "eta": "10 min"},
        {"name": "Swasthya Seva Clinic", "distance": "6.8 km", "eta": "15 min"},
        {"name": "Arogya Care Centre", "distance": "9.1 km", "eta": "19 min"},
    ]
    return random.choice(hospitals)

# First aid instructions
def get_first_aid(emergency_type):
    if emergency_type == "Cardiac Arrest":
        return "- Lay the person flat\n- Loosen clothing\n- Begin CPR if trained\n- Do not give food/water"
    elif emergency_type == "Breathing Problem":
        return "- Keep person upright\n- Encourage slow, deep breathing\n- Loosen clothes"
    else:
        return "Stay calm. Help is on the way. Provide comfort and avoid moving the patient unnecessarily."

# AI agent reply using GPT
def ai_response(user_msg):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI emergency assistant trained to respond to health emergencies."},
                {"role": "user", "content": user_msg}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return "⚠️ AI Agent unavailable. Please try again."

# Main Logic
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

    # Play emergency alert sound
    st.audio("assets/alert.mp3")

    st.markdown("---")
    st.subheader("🤖 AI Agent Response")
    st.markdown(ai_response(user_input))
else:
    st.warning("Please enter a statement to simulate an emergency.")

st.markdown("---")
st.caption("Made for Code for Bharat 🇮🇳 – AI that saves lives.")
