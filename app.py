import sys
sys.path.append('.')
import asyncio
import streamlit as st
import os
import speech_recognition as sr
import pyttsx3
from language_codes import LANGUAGES
from translator import translate

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

st.title("🌍 Language Translation GenAI App")

# Language selection
source_language = st.selectbox("Select Source Language", list(LANGUAGES.keys()))
target_language = st.selectbox("Select Target Language", list(LANGUAGES.keys()))
model_choice = st.selectbox("Choose Translation Model", ["Hugging Face", "Llama 3.2"])

# Text input for translation
sentence = st.text_area("Enter the Sentence to Translate")
translated_text = ""

# Translate button
if st.button("Translate"):
    if sentence.strip():
        with st.spinner("Translating..."):
            translated_text = translate(sentence, LANGUAGES[source_language], LANGUAGES[target_language], model_choice)
            st.success(f"Translated Text: {translated_text}")
    else:
        st.warning("Please enter a sentence to translate.")

# Speak translation button
def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1)
    engine.say(text)
    engine.runAndWait()

if st.button("🔊 Translate Audio to Text"):
    if translated_text:
        speak_text(translated_text)
    else:
        st.warning("Please translate some text first.")

# Audio file upload for translation
uploaded_file = st.file_uploader("Upload an audio file", type=["wav"])
if uploaded_file is not None:
    recognizer = sr.Recognizer()
    with sr.AudioFile(uploaded_file) as source:
        audio = recognizer.record(source)
        try:
            recognized_text = recognizer.recognize_google(audio)
            st.write(f"Recognized Speech: {recognized_text}")
            translated_text = translate(recognized_text, LANGUAGES[source_language], LANGUAGES[target_language], model_choice)
            st.success(f"Translated Text: {translated_text}")
        except sr.UnknownValueError:
            st.error("Could not understand audio.")
        except sr.RequestError:
            st.error("Speech recognition service error.")