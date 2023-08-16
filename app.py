import streamlit as st
import openai
from pydub import AudioSegment
import speech_recognition as sr
import requests
import os

# Retrieve the OpenAI API key from the secret
#OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]




# Set your OpenAI API key
openai.api_key = "OPENAI_API_KEY"
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


# # Streamlit App
# def main():
#     st.title("Podcast Summarizer")

#     st.write("Upload a podcast audio file for summarization.")
    
#     uploaded_file = st.file_uploader("Choose a podcast audio file", type=["mp3", "wav"])

#     if uploaded_file:
#         st.audio(uploaded_file, format="audio/wav")

#         if st.button("Summarize"):
#             st.write("Summarizing...")
            
#             # Prepare data for API call
#             audio_path = os.path.join("temp", uploaded_file.name)
#             uploaded_file.seek(0)
#             with open(audio_path, "wb+") as f:
#             #with open(audio_path, "wb") as f:
#                 f.write(uploaded_file.read())
            
#             # Call the backend API for information extraction and summarization
#             response = requests.post(BACKEND_API_ENDPOINT, files={"audio": open(audio_path, "rb")})
            
#             if response.status_code == 200:
#                 data = response.json()
#                 transcript = data["transcript"]
#                 extracted_info = data["extracted_info"]
#                 summary = data["summary"]
                
#                 st.write("Podcast Transcript:")
#                 st.write(transcript)
                
#                 st.write("Extracted Information:")
#                 st.write(extracted_info)
                
#                 st.write("Podcast Summary:")
#                 st.write(summary)
#             else:
#                 st.write("An error occurred during summarization.")

# if __name__ == "__main__":
#     main()
