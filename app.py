import streamlit as st
import json
import random
import time

st.set_page_config(page_title="🚑 AmbuBuddy: AI Emergency Dispatcher", layout="centered")
st.title("🚑 AmbuBuddy – AI-Powered Emergency Help (Bharat Focused)")

st.markdown("Speak or type your emergency in Hindi or English:")

# Emergency simulation inputs
user_input = st.text_input("👤 Your Statement (e.g., 'Papa ko heart attack ho gaya')", "")

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
    # Simulated hospital data
    hospitals = [
        {"name": "Jeevan Raksha Hospital", "distance": "4.2 km", "eta": "10 min"},
        {"name": "Swasthya Seva Clinic", "distance": "6.8 km", "eta": "15 min"},
        {"name": "Arogya Care Centre", "distance": "9.1 km", "eta": "19 min"},
    ]
    return random.choice(hospitals)

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
    if emergency_type == "Cardiac Arrest":
        st.markdown("""
        - Lay the person flat  
        - Loosen clothing  
        - Begin CPR if trained  
        - Do not give food/water  
        """)
    elif emergency_type == "Breathing Problem":
        st.markdown("""
        - Keep person upright  
        - Encourage slow, deep breathing  
        - Loosen clothes  
        """)
    else:
        st.markdown("Stay calm. Help is on the way. Provide comfort and avoid moving the patient unnecessarily.")

    st.audio("assets/alert.mp3")
else:
    st.warning("Please enter a statement to simulate an emergency.")

st.markdown("---")
st.caption("Made for Code for Bharat 🇮🇳 – AI that saves lives.")
