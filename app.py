import streamlit as st
import requests
import os

# Retrieve the OpenAI API key from the secret
#OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
OPENAI_API_KEY = "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" 


# Streamlit App
def main():
    st.title("Podcast Summarizer")

    st.write("Upload a podcast audio file for summarization.")
    
    uploaded_file = st.file_uploader("Choose a podcast audio file", type=["mp3", "wav"])

    if uploaded_file:
        st.audio(uploaded_file, format="audio/wav")

        if st.button("Summarize"):
            st.write("Summarizing...")
            
            # Prepare data for API call
            audio_path = os.path.join("temp", uploaded_file.name)
            uploaded_file.seek(0)
            with open(audio_path, "wb") as f:
                f.write(uploaded_file.read())
            
            # Call the backend API for information extraction and summarization
            response = requests.post(BACKEND_API_ENDPOINT, files={"audio": open(audio_path, "rb")})
            
            if response.status_code == 200:
                data = response.json()
                transcript = data["transcript"]
                extracted_info = data["extracted_info"]
                summary = data["summary"]
                
                st.write("Podcast Transcript:")
                st.write(transcript)
                
                st.write("Extracted Information:")
                st.write(extracted_info)
                
                st.write("Podcast Summary:")
                st.write(summary)
            else:
                st.write("An error occurred during summarization.")

if __name__ == "__main__":
    main()
