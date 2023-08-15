import openai
from getpass import getpass

openai.api_key = getpass('Enter the OpenAI API Key in the cell ')

import streamlit as st
import openai
from pydub import AudioSegment
import speech_recognition as sr

# Set your OpenAI API key
#openai.api_key = "YOUR_OPENAI_API_KEY"
openai.api_key = openai.api_key

def audio_to_text(audio_path):
    sound = AudioSegment.from_file(audio_path)
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_text = r.recognize_google(audio_data=source.record(sound))
    return audio_text

def summarize_podcast(podcast_text):
    prompt = f"Summarize the following podcast:\n{podcast_text}"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    summary = response.choices[0].text.strip()
    return summary

def main():
    st.title("Podcast Summarizer")

    st.write("Upload a podcast audio file (in WAV format) for summarization.")

    uploaded_file = st.file_uploader("Choose a WAV file", type="wav")

    if uploaded_file:
        st.audio(uploaded_file, format='audio/wav')

        if st.button("Summarize"):
            podcast_text = audio_to_text(uploaded_file)
            summary = summarize_podcast(podcast_text)
            st.write("Podcast Summary:")
            st.write(summary)

if __name__ == "__main__":
    main()

