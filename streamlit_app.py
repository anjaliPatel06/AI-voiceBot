import streamlit as st
import requests
import json

st.set_page_config(page_title="AI VoiceBot", layout="centered")

st.title(" AI Voice Bot")
st.write("Upload a WAV file to interact with the Voice Bot")

uploaded_file = st.file_uploader("Upload Audio File (.wav)", type=["wav"])

if uploaded_file is not None:

    st.audio(uploaded_file, format="audio/wav")

    if st.button("Process Voice"):

        with st.spinner("Processing..."):

            files = {
                "file": (uploaded_file.name, uploaded_file, "audio/wav")
            }

            try:
                response = requests.post(
                    "/voicebot",
                    files=files
                )

                result = response.json()

                st.success("Processing Complete ✅")

                st.subheader("Transcribed Text")
                st.write(result["transcribed_text"])

                st.subheader("Predicted Intent")
                st.write(result["intent"])
                st.write(f"Confidence: {result['confidence']:.2f}")

                st.subheader("Response Text")
                st.write(result["response_text"])

                st.subheader("Bot Audio Response")

                st.audio(result["audio_file_url"])

            except Exception as e:
                st.error(f"Error: {e}")
