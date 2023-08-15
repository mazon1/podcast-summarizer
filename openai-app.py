import streamlit as st
from pydub import AudioSegment
import speech_recognition as sr
import openai
import tempfile

# Set your OpenAI API key
#openai.api_key = st.secrets["openai_api_key"]


def audio_to_text(audio_path):
    sound = AudioSegment.from_mp3(audio_path)
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = source.record(sound)
        audio_text = r.recognize_google(audio_data=audio_data)
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
    st.write("Upload a podcast audio file (in MP3 format) for summarization.")
    uploaded_file = st.file_uploader("Choose an MP3 file", type="mp3")

    if uploaded_file:
        st.audio(uploaded_file, format='audio/mp3')

        if st.button("Summarize"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tmp_file.write(uploaded_file.read())
            podcast_text = audio_to_text(tmp_file.name)
            summary = summarize_podcast(podcast_text)
            st.write("Podcast Summary:")
            st.write(summary)

if __name__ == "__main__":
    main()
