import streamlit as st
from gtts import gTTS
import os
import whisper
import tempfile
from voice_utils import kurdish_chat_response

st.set_page_config(page_title="Kurdish Voice Assistant", layout="centered")
st.title("🗣 Kurdish Chatbot & Voice Assistant")

st.markdown("📢 Talk or type to the Kurdish chatbot!")

# Text input
user_input = st.text_input("Type something in Kurdish:")
if user_input:
    response = kurdish_chat_response(user_input)
    st.success("🤖: " + response)

    tts = gTTS(response, lang="ku")
    tts_file = "response.mp3"
    tts.save(tts_file)
    st.audio(tts_file, format='audio/mp3')

# Voice input
audio_file = st.file_uploader("Or upload Kurdish voice (.wav):", type=["wav"])
if audio_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    st.info("Transcribing...")
    model = whisper.load_model("base")
    result = model.transcribe(tmp_path)
    transcribed_text = result["text"]

    st.write("🗣 You said:", transcribed_text)

    response = kurdish_chat_response(transcribed_text)
    st.success("🤖: " + response)

    tts = gTTS(response, lang="ku")
    tts_file = "response_from_voice.mp3"
    tts.save(tts_file)
    st.audio(tts_file, format='audio/mp3')
